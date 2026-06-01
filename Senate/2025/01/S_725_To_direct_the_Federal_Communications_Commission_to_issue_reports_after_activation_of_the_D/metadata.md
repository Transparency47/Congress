# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/725?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/725
- Title: Enhancing First Response Act
- Congress: 119
- Bill type: S
- Bill number: 725
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-02-04T04:26:29Z
- Update date including text: 2026-02-04T04:26:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-59.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-59.
- 2025-09-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 146.
- 2025-09-10 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S6555; text of amendment in the nature of a substitute: CR S6555)
- 2025-09-10 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-09-11 - Floor: Message on Senate action sent to the House.
- 2025-09-11 10:57:03 - Floor: Received in the House.
- 2025-09-11 11:21:00 - Floor: Held at the desk.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-04-30 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-59.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-59.
- 2025-09-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 146.
- 2025-09-10 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S6555; text of amendment in the nature of a substitute: CR S6555)
- 2025-09-10 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-09-11 - Floor: Message on Senate action sent to the House.
- 2025-09-11 10:57:03 - Floor: Received in the House.
- 2025-09-11 11:21:00 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/725",
    "number": "725",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Enhancing First Response Act",
    "type": "S",
    "updateDate": "2026-02-04T04:26:29Z",
    "updateDateIncludingText": "2026-02-04T04:26:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-09-11",
      "actionTime": "11:21:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-09-11",
      "actionTime": "10:57:03",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S6555; text of amendment in the nature of a substitute: CR S6555)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 146.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-59.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-59.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2025-09-02T21:29:54Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-30T14:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-25T22:14:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NM"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AK"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NM"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WV"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NC"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-25",
      "state": "ME"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "SD"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "AZ"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ID"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "WA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s725is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 725\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Ms. Klobuchar (for herself, Mrs. Blackburn , Mr. Heinrich , Mr. Sullivan , Mr. Luj\u00e1n , Mrs. Capito , Mr. Markey , Mr. Budd , Mr. King , Mr. Thune , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Federal Communications Commission to issue reports after activation of the Disaster Information Reporting System and to make improvements to network outage reporting, to categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing First Response Act .\n#### 2. Reports after activation of disaster information reporting system; improvements to network outage reporting\n##### (a) Definitions\nIn this section:\n**(1) Automatic location information; automatic number identification**\nThe terms Automatic Location Information and Automatic Number Identification have the meanings given those terms in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Broadband internet access service**\nThe term broadband internet access service has the meaning given the term in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation.\n**(3) Commercial mobile service**\nThe term commercial mobile service has the meaning given the term in section 332(d) of the Communications Act of 1934 ( 47 U.S.C. 332(d) ).\n**(4) Commercial mobile data service**\nThe term commercial mobile data service has the meaning given the term in section 6001 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1401 ).\n**(5) Commission**\nThe term Commission means the Federal Communications Commission.\n**(6) Indian tribal government; local government**\nThe terms Indian tribal government and local government have the meanings given those terms in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(7) Interconnected VoIP service; State**\nThe terms interconnected VoIP service and State have the meanings given those terms in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ).\n**(8) Multi-line telephone system**\nThe term multi-line telephone system has the meaning given the term in section 721(f) of the Communications Act of 1934 ( 47 U.S.C. 623(f) ).\n**(9) Outage**\nThe term outage has the meaning given the term in section 4.5 of title 47, Code of Federal Regulations, or any successor regulation.\n**(10) Public safety answering point**\nThe term public safety answering point has the meaning given the term in section 222(h) of the Communications Act of 1934 ( 47 U.S.C. 222(h) ).\n**(11) System**\nThe term System means the Disaster Information Reporting System.\n##### (b) Reports after activation of disaster information reporting system\n**(1) Preliminary report**\n**(A) In general**\nNot later than 6 weeks after the deactivation of the System with respect to an event for which the System was activated for not less than 7 days, the Commission shall issue a preliminary report on, with respect to such event and to the extent known\u2014\n**(i)**\nthe number and duration of any outages of\u2014\n**(I)**\nbroadband internet access service;\n**(II)**\ninterconnected VoIP service;\n**(III)**\ncommercial mobile service; and\n**(IV)**\ncommercial mobile data service;\n**(ii)**\nthe approximate number of users or the amount of communications infrastructure potentially affected by an outage described in clause (i);\n**(iii)**\nthe number and duration of any outages that prevent public safety answering points from receiving caller location or number information or receiving emergency calls and routing such calls to emergency service personnel; and\n**(iv)**\nany additional information determined appropriate by the Commission.\n**(B) Development of report**\nThe Commission shall develop the report required by subparagraph (A) using information collected by the Commission, including information collected by the Commission through the System.\n**(2) Public field hearings**\n**(A) Requirement**\nNot later than 8 months after the deactivation of the System with respect to an event for which the System was activated for not less than 7 days, the Commission shall hold not less than 1 public field hearing in the area affected by such event.\n**(B) Inclusion of certain individuals in hearings**\nFor each public field hearing held under subparagraph (A), the Commission shall consider including\u2014\n**(i)**\nrepresentatives of State government, local government, or Indian tribal governments in areas affected by such event;\n**(ii)**\nresidents of the areas affected by such event, or consumer advocates;\n**(iii)**\nproviders of communications services affected by such event;\n**(iv)**\nfaculty of institutions of higher education;\n**(v)**\nrepresentatives of other Federal agencies;\n**(vi)**\nelectric utility providers;\n**(vii)**\ncommunications infrastructure companies; and\n**(viii)**\nfirst responders, emergency managers, or 9\u20131\u20131 directors in areas affected by such event.\n**(3) Final report**\nNot later than 12 months after the deactivation of the System with respect to an event for which the System was activated for not less than 7 days, the Commission shall issue a final report that includes, with respect to such event\u2014\n**(A)**\nthe information described in paragraph (1)(A); and\n**(B)**\nany recommendations of the Commission on how to improve the resiliency of affected communications or networks recovery efforts.\n**(4) Development of reports**\nIn developing a report required under this subsection, the Commission shall consider information collected by the Commission, including information collected by the Commission through the System, and any public hearing described in paragraph (2) with respect to the applicable event.\n**(5) Publication**\nThe Commission shall publish each report, excluding information that is otherwise exempt from public disclosure under the rules of the Commission, issued under this subsection on the website of the Commission upon the issuance of such report.\n##### (c) Improvements to network outage reporting\nNot later than 1 year after the date of enactment of this Act, the Commission shall investigate and publish a report on\u2014\n**(1)**\nthe value to public safety agencies of originating service providers including visual information to improve situational awareness about outages in the notifications provided to public safety answering points, as required by rules issued by the Commission;\n**(2)**\nthe volume and nature of 911 outages that may go unreported under the outage notification thresholds of the Commission; and\n**(3)**\nrecommended changes to rules issued by the Commission to address paragraphs (1) and (2).\n#### 3. Reporting of public safety telecommunicators as protective service occupations\n##### (a) Findings\nCongress finds the following:\n**(1)**\nPublic safety telecommunicators play a critical role in emergency response, providing medical instruction, gathering lifesaving information, and protecting civilians and first responders.\n**(2)**\nThe Standard Occupational Classification system is designed and maintained solely for statistical purposes, and is used by Federal statistical agencies to classify workers and jobs into occupational categories for the purpose of collecting, calculating, analyzing, or disseminating data.\n**(3)**\nOccupations in the Standard Occupational Classification are classified based on work performed and, in some cases, on the skills, education, or training needed to perform the work.\n**(4)**\nClassifying public safety telecommunicators as a protective service occupation would correct an inaccurate representation in the Standard Occupational Classification, recognize these professionals for the lifesaving work they perform, and better align the Standard Occupational Classification with related classification systems.\n##### (b) Standard Occupational Classification system\nThe Director of the Office of Management and Budget shall, not later than 30 days after the date of enactment of this Act, categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification system.\n#### 4. Report on implementation of the Kari\u2019s Law Act of 2017\nNot later than 180 days after the date of enactment of this Act, the Inspector General of the Commission shall publish a report regarding the enforcement by the Commission of section 721 of the Communications Act of 1934 ( 47 U.S.C. 623 ), which shall include\u2014\n**(1)**\na summary of the extent to which multi-line telephone system manufacturers and vendors have complied with that section;\n**(2)**\npotential difficulties and obstacles in complying with that section;\n**(3)**\nrecommendations to the Commission, if necessary, on ways to improve the policies of the Commission to better enforce that section; and\n**(4)**\nrecommendations to Congress, if necessary, on further legislation that could mitigate problems like those that are addressed by that section.",
      "versionDate": "2025-02-25",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s725rs.xml",
      "text": "II\nCalendar No. 146\n119th CONGRESS\n1st Session\nS. 725\n[Report No. 119\u201359]\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Ms. Klobuchar (for herself, Mrs. Blackburn , Mr. Heinrich , Mr. Sullivan , Mr. Luj\u00e1n , Mrs. Capito , Mr. Markey , Mr. Budd , Mr. King , Mr. Thune , Mr. Kelly , Mr. Crapo , and Ms. Cantwell ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 2, 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo direct the Federal Communications Commission to issue reports after activation of the Disaster Information Reporting System and to make improvements to network outage reporting, to categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing First Response Act .\n#### 2. Reports after activation of disaster information reporting system; improvements to network outage reporting\n##### (a) Definitions\nIn this section:\n**(1) Automatic location information; automatic number identification**\nThe terms Automatic Location Information and Automatic Number Identification have the meanings given those terms in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Broadband internet access service**\nThe term broadband internet access service has the meaning given the term in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation.\n**(3) Commercial mobile service**\nThe term commercial mobile service has the meaning given the term in section 332(d) of the Communications Act of 1934 ( 47 U.S.C. 332(d) ).\n**(4) Commercial mobile data service**\nThe term commercial mobile data service has the meaning given the term in section 6001 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1401 ).\n**(5) Commission**\nThe term Commission means the Federal Communications Commission.\n**(6) Indian tribal government; local government**\nThe terms Indian tribal government and local government have the meanings given those terms in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(7) Interconnected VoIP service; State**\nThe terms interconnected VoIP service and State have the meanings given those terms in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ).\n**(8) Multi-line telephone system**\nThe term multi-line telephone system has the meaning given the term in section 721(f) of the Communications Act of 1934 ( 47 U.S.C. 623(f) ).\n**(9) Outage**\nThe term outage has the meaning given the term in section 4.5 of title 47, Code of Federal Regulations, or any successor regulation.\n**(10) Public safety answering point**\nThe term public safety answering point has the meaning given the term in section 222(h) of the Communications Act of 1934 ( 47 U.S.C. 222(h) ).\n**(11) System**\nThe term System means the Disaster Information Reporting System.\n##### (b) Reports after activation of disaster information reporting system\n**(1) Preliminary report**\n**(A) In general**\nNot later than 6 weeks after the deactivation of the System with respect to an event for which the System was activated for not less than 7 days, the Commission shall issue a preliminary report on, with respect to such event and to the extent known\u2014\n**(i)**\nthe number and duration of any outages of\u2014\n**(I)**\nbroadband internet access service;\n**(II)**\ninterconnected VoIP service;\n**(III)**\ncommercial mobile service; and\n**(IV)**\ncommercial mobile data service;\n**(ii)**\nthe approximate number of users or the amount of communications infrastructure potentially affected by an outage described in clause (i);\n**(iii)**\nthe number and duration of any outages that prevent public safety answering points from receiving caller location or number information or receiving emergency calls and routing such calls to emergency service personnel; and\n**(iv)**\nany additional information determined appropriate by the Commission.\n**(B) Development of report**\nThe Commission shall develop the report required by subparagraph (A) using information collected by the Commission, including information collected by the Commission through the System.\n**(2) Public field hearings**\n**(A) Requirement**\nNot later than 8 months after the deactivation of the System with respect to an event for which the System was activated for not less than 7 days, the Commission shall hold not less than 1 public field hearing in the area affected by such event.\n**(B) Inclusion of certain individuals in hearings**\nFor each public field hearing held under subparagraph (A), the Commission shall consider including\u2014\n**(i)**\nrepresentatives of State government, local government, or Indian tribal governments in areas affected by such event;\n**(ii)**\nresidents of the areas affected by such event, or consumer advocates;\n**(iii)**\nproviders of communications services affected by such event;\n**(iv)**\nfaculty of institutions of higher education;\n**(v)**\nrepresentatives of other Federal agencies;\n**(vi)**\nelectric utility providers;\n**(vii)**\ncommunications infrastructure companies; and\n**(viii)**\nfirst responders, emergency managers, or 9\u20131\u20131 directors in areas affected by such event.\n**(3) Final report**\nNot later than 12 months after the deactivation of the System with respect to an event for which the System was activated for not less than 7 days, the Commission shall issue a final report that includes, with respect to such event\u2014\n**(A)**\nthe information described in paragraph (1)(A); and\n**(B)**\nany recommendations of the Commission on how to improve the resiliency of affected communications or networks recovery efforts.\n**(4) Development of reports**\nIn developing a report required under this subsection, the Commission shall consider information collected by the Commission, including information collected by the Commission through the System, and any public hearing described in paragraph (2) with respect to the applicable event.\n**(5) Publication**\nThe Commission shall publish each report, excluding information that is otherwise exempt from public disclosure under the rules of the Commission, issued under this subsection on the website of the Commission upon the issuance of such report.\n##### (c) Improvements to network outage reporting\nNot later than 1 year after the date of enactment of this Act, the Commission shall investigate and publish a report on\u2014\n**(1)**\nthe value to public safety agencies of originating service providers including visual information to improve situational awareness about outages in the notifications provided to public safety answering points, as required by rules issued by the Commission;\n**(2)**\nthe volume and nature of 911 outages that may go unreported under the outage notification thresholds of the Commission; and\n**(3)**\nrecommended changes to rules issued by the Commission to address paragraphs (1) and (2).\n#### 3. Reporting of public safety telecommunicators as protective service occupations\n##### (a) Findings\nCongress finds the following:\n**(1)**\nPublic safety telecommunicators play a critical role in emergency response, providing medical instruction, gathering lifesaving information, and protecting civilians and first responders.\n**(2)**\nThe Standard Occupational Classification system is designed and maintained solely for statistical purposes, and is used by Federal statistical agencies to classify workers and jobs into occupational categories for the purpose of collecting, calculating, analyzing, or disseminating data.\n**(3)**\nOccupations in the Standard Occupational Classification are classified based on work performed and, in some cases, on the skills, education, or training needed to perform the work.\n**(4)**\nClassifying public safety telecommunicators as a protective service occupation would correct an inaccurate representation in the Standard Occupational Classification, recognize these professionals for the lifesaving work they perform, and better align the Standard Occupational Classification with related classification systems.\n##### (b) Standard Occupational Classification system\nThe Director of the Office of Management and Budget shall, not later than 30 days after the date of enactment of this Act, categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification system.\n#### 4. Report on implementation of the Kari\u2019s Law Act of 2017\nNot later than 180 days after the date of enactment of this Act, the Inspector General of the Commission shall publish a report regarding the enforcement by the Commission of section 721 of the Communications Act of 1934 ( 47 U.S.C. 623 ), which shall include\u2014\n**(1)**\na summary of the extent to which multi-line telephone system manufacturers and vendors have complied with that section;\n**(2)**\npotential difficulties and obstacles in complying with that section;\n**(3)**\nrecommendations to the Commission, if necessary, on ways to improve the policies of the Commission to better enforce that section; and\n**(4)**\nrecommendations to Congress, if necessary, on further legislation that could mitigate problems like those that are addressed by that section.",
      "versionDate": "2025-09-02",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s725es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 725\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo direct the Federal Communications Commission to issue reports after activation of the Disaster Information Reporting System and to make improvements to network outage reporting, to categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing First Response Act .\n#### 2. Reports after activation of disaster information reporting system; improvements to network outage reporting\n##### (a) Definitions\nIn this section:\n**(1) Automatic location information; automatic number identification**\nThe terms Automatic Location Information and Automatic Number Identification have the meanings given those terms in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Broadband internet access service**\nThe term broadband internet access service has the meaning given the term in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation.\n**(3) Commercial mobile service**\nThe term commercial mobile service has the meaning given the term in section 332(d) of the Communications Act of 1934 ( 47 U.S.C. 332(d) ).\n**(4) Commercial mobile data service**\nThe term commercial mobile data service has the meaning given the term in section 6001 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1401 ).\n**(5) Commission**\nThe term Commission means the Federal Communications Commission.\n**(6) Indian tribal government; local government**\nThe terms Indian tribal government and local government have the meanings given those terms in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(7) Interconnected VoIP service**\nThe term interconnected VoIP service has the meaning given that term in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(8) Multi-line telephone system**\nThe term multi-line telephone system has the meaning given the term in section 721(f) of the Communications Act of 1934 ( 47 U.S.C. 623(f) ).\n**(9) Outage**\nThe term outage has the meaning given the term in section 4.5 of title 47, Code of Federal Regulations, or any successor regulation.\n**(10) Public safety answering point**\nThe term public safety answering point has the meaning given the term in section 222(h) of the Communications Act of 1934 ( 47 U.S.C. 222(h) ).\n**(11) State**\nThe term State has the meaning given that term in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 ).\n**(12) System**\nThe term System means the Disaster Information Reporting System.\n##### (b) Reports after activation of the disaster information reporting system\n**(1) Public hearings**\n**(A) Requirement**\nEach year, the Commission shall hold not less than 1 public hearing relating to all events during the preceding 1-year period for which the System was activated for not less than 7 days.\n**(B) Inclusion of certain individuals in public hearings**\nFor each public hearing held under subparagraph (A), the Commission shall consider including\u2014\n**(i)**\nrepresentatives of State government, local government, or Indian tribal governments in areas affected by such event;\n**(ii)**\nresidents of the areas affected by such event, or consumer advocates;\n**(iii)**\nproviders of communications services affected by such event;\n**(iv)**\nfaculty of institutions of higher education;\n**(v)**\nrepresentatives of other Federal agencies;\n**(vi)**\nelectric utility providers;\n**(vii)**\ncommunications infrastructure companies; and\n**(viii)**\nfirst responders, emergency managers, and 911 directors in areas affected by such event.\n**(2) Report**\nNot later than 120 days after the public hearing under paragraph (1) occurs, the Commission shall issue a report that includes, with respect to such event and to the extent known without requiring the collection of additional information\u2014\n**(A)**\nthe number and duration of any outages of\u2014\n**(i)**\nbroadband internet access service;\n**(ii)**\ninterconnected VoIP service;\n**(iii)**\ncommercial mobile service; and\n**(iv)**\ncommercial mobile data service;\n**(B)**\nthe approximate number of users and the amount of communications infrastructure potentially affected by an outage described in subparagraph (A);\n**(C)**\nthe number and duration of any outages that prevent public safety answering points from receiving caller location or number information or receiving emergency calls and routing such calls to emergency service personnel; and\n**(D)**\nany recommendations of the Commission on how to improve the resiliency of affected communications or networks recovery efforts.\n**(3) Development of reports**\nIn developing a report required under paragraph (2), the Commission shall consider information collected by the Commission, including information collected by the Commission through the System, and any public hearing described in paragraph (1) with respect to the applicable event.\n**(4) Publication**\nThe Commission shall publish each report, excluding information that is otherwise exempt from public disclosure under the rules of the Commission or was submitted to the Commission with a proper request for confidential treatment as described in section 0.459 of title 47, Code of Federal Regulations, issued under this subsection on the website of the Commission upon the issuance of such report. The Commission shall not publicly disclose company-specific information.\n##### (c) Improvements to network outage reporting\nNot later than 1 year after the date of enactment of this Act, the Commission shall investigate and publish a report on\u2014\n**(1)**\nthe value to public safety agencies of originating service providers including visual information to improve situational awareness about outages in the notifications provided to public safety answering points, as required by rules issued by the Commission;\n**(2)**\nthe volume and nature of 911 outages that may go unreported under the outage notification thresholds of the Commission;\n**(3)**\nthe balance between the value described in paragraph (1) to public safety agencies and the burden and practicality for originating service providers of including visual information in outage notifications as described in that paragraph; and\n**(4)**\nrecommended changes to rules issued by the Commission to address paragraphs (1) and (2).\n##### (d) Rule of construction\nNothing in this Act shall be construed to provide the Commission or any other person authority over any provider of broadband internet access service beyond what is specifically authorized under this Act.\n#### 3. Reporting of public safety telecommunicators as protective service occupations\n##### (a) Findings\nCongress finds the following:\n**(1)**\nPublic safety telecommunicators play a critical role in emergency response, providing medical instruction, gathering lifesaving information, and protecting civilians and first responders.\n**(2)**\nThe Standard Occupational Classification system is designed and maintained solely for statistical purposes, and is used by Federal statistical agencies to classify workers and jobs into occupational categories for the purpose of collecting, calculating, analyzing, or disseminating data.\n**(3)**\nOccupations in the Standard Occupational Classification are classified based on work performed and, in some cases, on the skills, education, or training needed to perform the work.\n**(4)**\nClassifying public safety telecommunicators as a protective service occupation would correct an inaccurate representation in the Standard Occupational Classification, recognize these professionals for the lifesaving work they perform, and better align the Standard Occupational Classification with related classification systems.\n##### (b) Standard Occupational Classification system\nThe Director of the Office of Management and Budget shall, not later than 30 days after the date of enactment of this Act, categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification system.\n#### 4. Report on implementation of the Kari\u2019s Law Act of 2017\nNot later than 180 days after the date of enactment of this Act, the Commission shall publish a report regarding the enforcement by the Commission of section 721 of the Communications Act of 1934 ( 47 U.S.C. 623 ), which shall include\u2014\n**(1)**\na summary of the extent to which multi-line telephone system manufacturers and vendors have complied with that section;\n**(2)**\npotential difficulties and obstacles in complying with that section;\n**(3)**\nrecommendations to the Commission, if necessary, on ways to improve the policies of the Commission to better enforce that section; and\n**(4)**\nrecommendations to Congress, if necessary, on further legislation that could mitigate problems like those that are addressed by that section.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-12T15:21:53Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-05-12T15:15:43Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-05-12T15:21:35Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-05-12T15:22:19Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-12T15:16:12Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-12T15:21:43Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-05-12T15:20:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-21T18:39:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s725",
          "measure-number": "725",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s725v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Enhancing First Response Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to report on certain activations of the Disaster Information Reporting System (DIRS). DIRS is a reporting system that\u00a0is activated during severe weather and other events impacting communications service and enables communications providers to report outages and other degradations to service.</p><p>If the system was activated for at least seven days, the FCC must issue a preliminary report that includes information about the number, duration, and nature of all associated outages. The FCC must also hold at least one public field hearing in the area affected by the event, and it must issue a final report that includes recommendations for improving the resiliency of affected networks or recovery efforts.</p><p>Separately, the FCC must publish a general report on (1) the volume and nature of 9-1-1 outages that are not required to be reported under current outage notification rules, and (2) the value to public safety agencies of the inclusion of visual information in outage notifications from communications providers.</p><p>The bill also requires the Office of Management and Budget, by 30 days after the bill's enactment, to categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification System.</p><p>Finally, the Office of the\u00a0Inspector General of the FCC is directed\u00a0to publish a report on the implementation of Kari\u2019s Law, which requires multiline telephone systems to be preconfigured to allow users to dial 9-1-1 directly from any phone without dialing any additional code or prefix.</p>"
        },
        "title": "Enhancing First Response Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s725.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Enhancing First Response Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to report on certain activations of the Disaster Information Reporting System (DIRS). DIRS is a reporting system that\u00a0is activated during severe weather and other events impacting communications service and enables communications providers to report outages and other degradations to service.</p><p>If the system was activated for at least seven days, the FCC must issue a preliminary report that includes information about the number, duration, and nature of all associated outages. The FCC must also hold at least one public field hearing in the area affected by the event, and it must issue a final report that includes recommendations for improving the resiliency of affected networks or recovery efforts.</p><p>Separately, the FCC must publish a general report on (1) the volume and nature of 9-1-1 outages that are not required to be reported under current outage notification rules, and (2) the value to public safety agencies of the inclusion of visual information in outage notifications from communications providers.</p><p>The bill also requires the Office of Management and Budget, by 30 days after the bill's enactment, to categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification System.</p><p>Finally, the Office of the\u00a0Inspector General of the FCC is directed\u00a0to publish a report on the implementation of Kari\u2019s Law, which requires multiline telephone systems to be preconfigured to allow users to dial 9-1-1 directly from any phone without dialing any additional code or prefix.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119s725"
    },
    "title": "Enhancing First Response Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Enhancing First Response Act</strong></p><p>This bill requires the Federal Communications Commission (FCC) to report on certain activations of the Disaster Information Reporting System (DIRS). DIRS is a reporting system that\u00a0is activated during severe weather and other events impacting communications service and enables communications providers to report outages and other degradations to service.</p><p>If the system was activated for at least seven days, the FCC must issue a preliminary report that includes information about the number, duration, and nature of all associated outages. The FCC must also hold at least one public field hearing in the area affected by the event, and it must issue a final report that includes recommendations for improving the resiliency of affected networks or recovery efforts.</p><p>Separately, the FCC must publish a general report on (1) the volume and nature of 9-1-1 outages that are not required to be reported under current outage notification rules, and (2) the value to public safety agencies of the inclusion of visual information in outage notifications from communications providers.</p><p>The bill also requires the Office of Management and Budget, by 30 days after the bill's enactment, to categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification System.</p><p>Finally, the Office of the\u00a0Inspector General of the FCC is directed\u00a0to publish a report on the implementation of Kari\u2019s Law, which requires multiline telephone systems to be preconfigured to allow users to dial 9-1-1 directly from any phone without dialing any additional code or prefix.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119s725"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s725is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s725rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s725es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Enhancing First Response Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Enhancing First Response Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-09-11T04:53:20Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Enhancing First Response Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-04T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Enhancing First Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Federal Communications Commission to issue reports after activation of the Disaster Information Reporting System and to make improvements to network outage reporting, to categorize public safety telecommunicators as a protective service occupation under the Standard Occupational Classification system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:00Z"
    }
  ]
}
```
