class Chatbot:
    def get_response(self, user_input):
        # Convert input to lowercase for case-insensitive comparison
        user_input = user_input.lower()

        # Simple rule-based logic for generating responses
        if "hello" in user_input:
            return "Hello! How can I assist you?"
        elif "performance" in user_input:
            return "You can check your performance in the dashboard."
        elif "project review" in user_input:
            return "Monthly project reviews are scheduled on 19 Oct. Do you need any help regarding it?"
        elif "faculty advisor" in user_input:
            return "You can contact your faculty advisor in working hours only . If you need specific contact details, let me know!"
        elif "Parent meeting" in user_input:
            return "Yes meeting is schedule on 3 oct. If you're looking for specific meetings, let me know, and I can help find the details"
        elif "semester project" in user_input:
            return "Project submission of final projects is schedule after the Upcoming unit test"
        elif "academic calendar" in user_input:
            return "The academic calendar is available in the college WhatsApp group if you want to join contact 8787888787 . It includes important dates like exam schedules and holidays. Need help finding it?"
        elif "college events" in user_input:
            return "Yes, from next month our college is organizing college fest and Hackathon. Would you like me to guide you there?"
        else:
            return "I'm not sure how to answer that. Can you try asking something else?"
