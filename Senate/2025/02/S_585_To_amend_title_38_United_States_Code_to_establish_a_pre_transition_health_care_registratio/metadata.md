# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/585?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/585
- Title: Servicemember to Veteran Health Care Connection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 585
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-03-19T11:03:25Z
- Update date including text: 2026-03-19T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/585",
    "number": "585",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Servicemember to Veteran Health Care Connection Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:25Z",
    "updateDateIncludingText": "2026-03-19T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
            "date": "2025-05-21T20:00:06Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:06Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-13T18:10:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ND"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s585is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 585\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. King (for himself, Mr. Rounds , Mr. Cramer , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish a pre-transition health care registration process to facilitate enrollment in the patient enrollment system of the Department of Veterans Affairs by members of the Armed Forces who are separating from the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemember to Veteran Health Care Connection Act of 2025 .\n#### 2. Pre-transition health care registration of members of the Armed Forces to streamline receipt of health care from Department of Veterans Affairs\n##### (a) Health care pre-Registration\n**(1) In general**\nSubchapter I of chapter 17 of title 38, United States Code, is amended by inserting after section 1705A the following new section:\n1705B. Management of health care: registration in pre-transition system and facilitation of enrollment (a) Pre-Transition system (1) In general Not later than 180 days before the anticipated separation from the Armed Forces of a member of the Armed Forces, the Secretary shall automatically register such member in the pre-transition health care registration system. (2) Registration Registration of a member of the Armed Forces in the pre-transition health care registration system under paragraph (1) shall consist of the entry of relevant information of such member into such system so as to facilitate and permit, at a future date, a final determination with respect to the enrollment of such member in the patient enrollment system if such member elects to enroll in the patient enrollment system and is eligible to enroll in the patient enrollment system. (b) Facilitation of enrollment in patient enrollment system (1) In general Not later than 30 days after separation of a covered individual from the Armed Forces, or as soon as feasibly possible following such separation, the Secretary shall engage with such individual\u2014 (A) to assist and facilitate the completion of the process for enrollment of such individual in the patient enrollment system, to include the appropriate electronic or paper forms; and (B) to schedule an initial primary care or other health appointment for such individual under the laws administered by the Secretary if the individual is interested in such an appointment. (2) Communication efforts Communication to a covered individual under paragraph (1) shall be conducted through a combination of effective mechanisms to include by electronic means through email and text message, paper mail, and by phone. (3) Covered individual defined In this subsection, the term covered individual means an individual who\u2014 (A) is eligible for or expected to be eligible for enrollment in the patient enrollment system; and (B) is not yet enrolled in such system. (c) Outreach (1) Pre-transition (A) In general To the greatest extent feasible, the Secretary shall conduct timely outreach to members of the Armed Forces registered in the pre-transition health care registration system, in advance of their separation from the Armed Forces, to explain\u2014 (i) what such registration means in practical terms; (ii) what steps each such member will need to take after separation from the Armed Forces to fully enroll, if eligible, in the patient enrollment system; (iii) health care services that may be available to such member upon enrollment in such system, including the general rules of eligibility for such services; (iv) health care services that may be available to such member regardless of enrollment in such system, including counseling for military sexual trauma and services from Vet Centers (as defined in section 1712A of this title), including the general rules of eligibility for such services; and (v) the steps required to access services described in clauses (iii) and (iv). (B) Outreach efforts Outreach to a member of the Armed Forces required under subparagraph (A) shall be conducted through a combination of effective mechanisms, including by electronic means through email and text message, paper mail, and by phone. (2) After enrollment (A) In general Not less frequently than once during the 180-day period following the enrollment of an individual in the patient enrollment system, the Secretary shall contact any such individual who has not scheduled a primary care appointment or other health appointment under the laws administered by the Secretary and offer to schedule such appointment should such individual be interested in doing so. (B) Conduct of outreach The Secretary may conduct outreach under subparagraph (A) as part of the Solid Start program under section 6320 of this title, other existing processes of the Department, or any new process as the Secretary determines appropriate. (d) Definitions In this section: (1) Patient enrollment system The term patient enrollment system means the system of annual patient enrollment of the Department established and operated under section 1705(a) of this title. (2) Pre-transition health care registration system The term pre-transition health care registration system means an information technology or other system or systems of the Department in which the Department enters or stores the relevant information of a transitioning member of the Armed Forces so as to facilitate and permit, at a future date, a final enrollment determination with respect to the enrollment of such member in the patient enrollment system. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1705A the following new item:\n1705B. Management of health care: registration in pre-transition system and facilitation of enrollment. .\n**(3) Effective date**\nThis subsection and the amendments made by this subsection shall take effect on the date of the enactment of this Act and apply to any member of the Armed Forces who is anticipated to separate from the Armed Forces on and after the date that is one year after the date of the enactment of this Act.\n##### (b) Establishment of system\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Secretary of Defense, shall establish and implement an automated process to implement the pre-transition health care registration system required under section 1705B(a) of title 38, United States Code, as added by subsection (a)(1).\n**(2) Briefings on initial implementation**\nNot later than each of 180 days, one year, and two years after the date of the enactment of this Act, the Department of Veterans Affairs-Department of Defense Joint Executive Committee established under section 320 of title 38, United States Code, shall provide to the appropriate committees of Congress a briefing on the implementation of the process required under paragraph (1).\n##### (c) Coordination with Department of Defense\n**(1) In general**\nIn implementing the requirements of this section and the amendments made by this section, the Secretary of Veterans Affairs may integrate and coordinate such implementation with the Solid Start program of the Department of Veterans Affairs under section 6320 of title 38, United States Code, other existing processes of the Department, or any new process as the Secretary determines appropriate to ensure collaboration and coordination with relevant programs of the Department of Defense.\n**(2) Inclusion in Transition Assistance Program**\nOn and after the date that is one year after the date of the enactment of this Act, the Secretary of Defense shall include an explanation of the pre-transition health care registration system required under section 1705B of title 38, United States Code, as added by subsection (a)(1), as part of the Transition Assistance Program of the Department of Defense.\n##### (d) Requirement to create and maintain simple and streamlined process for pre-Registration and enrollment\n**(1) In general**\nThe Secretary of Veterans Affairs shall make enrollment in the patient enrollment system, including pre-transition health care registration under section 1705B of title 38, United States Code, as added by subsection (a)(1), a simple and streamlined process for all transitioning members of the Armed Forces and veterans\u2014\n**(A)**\nto facilitate access to and utilization of services from the Department of Veterans Affairs to which such individuals are entitled;\n**(B)**\nto ensure such individuals have a healthy and smooth transition out of the Armed Forces into civilian life as veterans;\n**(C)**\nto support the mental and physical health of such individuals; and\n**(D)**\nto reduce, to the greatest extent possible, veteran suicide.\n**(2) Improvement of process**\nThe Secretary shall continuously monitor, improve, and modernize the process described in paragraph (1).\n##### (e) Outreach and engagement\nThe Secretary of Veterans Affairs shall\u2014\n**(1)**\nproactively conduct outreach to transitioning and recently transitioned members of the Armed Forces to assist such members in enrolling in the patient enrollment system;\n**(2)**\nproactively and regularly engage with veterans already enrolled in the patient enrollment system to offer assistance in accessing health care services under such system;\n**(3)**\nproactively and regularly engage with veterans who may not be eligible for enrollment in the patient enrollment system but may be eligible to access certain specific health services of the Department;\n**(4)**\nproactively engage with veterans from traditionally under-represented groups, to include women veterans, minority veterans, Native American veterans, Native Hawaiian veterans, Alaska Native veterans, and LGBTQIA+ veterans; and\n**(5)**\nengage with veterans who are eligible but not enrolled in the patient enrollment system and offer information and assistance regarding the steps to facilitate enrollment in such system.\n##### (f) Annual report on pre-Transition registration\nSection 8111(f)(2) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraphs (E) and (F) as subparagraphs (F) and (G), respectively; and\n**(2)**\nby inserting after subparagraph (D) the following new subparagraph (E):\n(E) With respect to the registration of members of the Armed Forces in the pre-transition health care registration system under section 1705B of this title during the preceding fiscal year, the following: (i) The number of members of the Armed Forces who were registered in such system. (ii) The number of such members who subsequently applied for enrollment in the system of annual patient enrollment of the Department established and operated under section 1705(a) of this title. (iii) The aggregated disposition of each such application for enrollment, whether denied or approved, and a reason for any denial, if available. (iv) Aggregated demographic information for members of the Armed Forces described in clauses (i) and (ii), including age, gender, ethnicity, length of service, military rank, and branch of service. (v) Any information on health care utilization rates based on registration in the pre-transition health care registration system under section 1705B of this title that the Secretary considers relevant. (vi) Any additional observations or information the Secretary considers relevant regarding the impact of pre-transition health care registration on streamlining and improving the transition from the Armed Forces to civilian life. .\n##### (g) Reports\n**(1) Report on feasibility and advisability of permitting members of the Armed Forces to receive pre-separation health appointment with Department of Veterans Affairs**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Secretary of Defense, shall submit to the appropriate committees of Congress a report on the feasibility and advisability of permitting transitioning members of the Armed Forces, including those on separation leave, while still on active duty, to receive at least one no-cost health care appointment at a facility of the Department of Veterans Affairs\u2014\n**(i)**\nto familiarize the member with the health services of the Department prior to the member leaving the Armed Forces; and\n**(ii)**\nto improve the transition process and health and wellness of the member once they have transitioned to civilian life.\n**(B) Elements**\nThe report required under subparagraph (A) shall include the following:\n**(i)**\nA description of the reasons the Secretary of Veterans Affairs has determined the policy described in such subparagraph is feasible and advisable or not.\n**(ii)**\nAn identification of changes to law that would be required or recommended to make such policy feasible and advisable.\n**(iii)**\nIf the Secretary determines such policy is feasible and advisable, a proposed schedule and timeline to implement such policy and an estimate of costs to implement and sustain such policy.\n**(iv)**\nSuch other information as the Secretary considers appropriate.\n**(2) Report on efforts to improve enrollment**\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Secretary of Defense, shall submit to the appropriate committees of Congress a report containing the following:\n**(A)**\nAn assessment of the efforts of the Secretary of Veterans Affairs as follows:\n**(i)**\nTo develop and implement a system or systems, and processes to implement such a system or systems, to notify veterans who receive a positive adjudication for a service-connected disability and are not already enrolled in the patient enrollment system regarding how to enroll in the patient enrollment system, should they be inclined to enroll.\n**(ii)**\nTo pre-populate information in the pre-transition health care registration system required under section 1705B of title 38, United States Code, as added by subsection (a)(1), using data available within the Department of Veterans Affairs, other Federal agencies, or State agencies or other appropriate commercial or publicly available information so as to assist transitioning members of the Armed Forces with completing the process of enrollment in the patient enrollment system, and to simplify and streamline enrollment in such system, including\u2014\n**(I)**\na description of any roadblocks to pre-populating such information;\n**(II)**\na description of any challenges in receiving relevant information from any Federal agency or State agency; and\n**(III)**\nan identification of any legislative action that may be required to improve the collection of data necessary to carry out this clause.\n**(B)**\nAn assessment of any challenges experienced by the Secretary of Veterans Affairs in receiving timely and reliable electronic information, data feeds, and notifications from the Department of Defense, other Federal agencies, or non-Federal entities regarding the separation from the Armed Forces of members of the Armed Forces, including\u2014\n**(i)**\nspecific requests for legislative action to improve data transmission from the Department of Defense or other Federal agencies to the Department of Veterans Affairs; and\n**(ii)**\na description of policy reforms to require the military departments to report to the Secretary of Defense known or anticipated separations in a more timely manner.\n**(C)**\nThe identification of an individual in a Senior Executive Service position (as defined in section 3132(a) of title 5, United States Code), or equivalent, and office within the Department of Veterans Affairs that is coordinating or will coordinate all programs of the Department relating to improving the registration and enrollment of transitioning or transitioned members of the Armed Forces in health care services of the Department (including pursuant to this section and the amendments made by this section) and the usage by such members of those services, to include the following programs and offices:\n**(i)**\nThe Solid Start program of the Department under section 6320 of title 38, United States Code.\n**(ii)**\nThe Federal Recovery Consultant Office of the Department.\n**(iii)**\nThe Post-9/11 Military2VA Case Management Program of the Department.\n**(iv)**\nThe Liaison Program of the Department.\n**(v)**\nThe Concierge for Care Program of the Department.\n**(vi)**\nThe office of the Department responsible for carrying out the pre-transition health care registration system under section 1705B of title 38, United States Code, as added by subsection (a)(1).\n**(vii)**\nOther similar or successor programs or offices of the Department.\n**(D)**\nA description of how the individual and office identified under subparagraph (C) manages or will manage various programs across the Department, to include\u2014\n**(i)**\nprograms under the Veterans Health Administration, Veterans Benefits Administration, and other entities of the Department that have different reporting chains;\n**(ii)**\nan identification of metrics that are used or will be used to monitor program goals;\n**(iii)**\nan identification of steps that can be taken to improve management and outcomes of such programs, to include collaboration and coordination with relevant programs of the Department of Defense; and\n**(iv)**\nan organizational chart to show how efforts described under this subparagraph are managed across the Department of Veterans Affairs.\n##### (h) Rule of construction\nNothing in this section or the amendments made by this section shall be construed to require any member of the Armed Forces, former member of the Armed Forces, or veteran to use any service of the Department of Veterans Affairs or to enroll in the patient enrollment system.\n##### (i) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Veterans Affairs\u2019 of the Senate; and\n**(B)**\nthe Committee on Armed Services and the Committee on Veterans Affairs\u2019 of the House of Representatives.\n**(2) Patient enrollment system**\nThe term patient enrollment system means the system of annual patient enrollment of the Department established and operated under section 1705(a) of title 38, United States Code.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
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
            "name": "Computers and information technology",
            "updateDate": "2025-06-02T20:14:19Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-02T20:14:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-02T20:14:31Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-02T20:14:04Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-06-02T20:14:11Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-02T20:13:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:41:26Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s585is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Servicemember to Veteran Health Care Connection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Servicemember to Veteran Health Care Connection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to establish a pre-transition health care registration process to facilitate enrollment in the patient enrollment system of the Department of Veterans Affairs by members of the Armed Forces who are separating from the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:28Z"
    }
  ]
}
```
