# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3976?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3976
- Title: NCAA Accountability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3976
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-01-14T05:00:20Z
- Update date including text: 2026-01-14T05:00:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3976",
    "number": "3976",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "NCAA Accountability Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T05:00:20Z",
    "updateDateIncludingText": "2026-01-14T05:00:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
        "item": {
          "date": "2025-06-12T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3976ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3976\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Kustoff (for himself, Mr. Harder of California , and Mr. Owens ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish due process requirements for the investigation of intercollegiate athletics, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NCAA Accountability Act of 2025 .\n#### 2. Due process requirements\n##### (a) In general\nEach covered athletic association shall establish and administer due process requirements for the investigation of any member institution, student athlete enrolled in such member institution, or other individual for any alleged infraction of the covered athletic association\u2019s bylaws or failure to meet the conditions and obligations of membership if the matter cannot be resolved without a formal investigation, consistent with the following:\n**(1)**\nIf the covered athletic association or any governing body subordinate to the covered athletic association, initiates an investigation whether formal or informal into a member institution, the covered athletic association shall provide written notice to the member institution detailing the nature of the inquiry by not later than 60 days after the covered athletic association receives information indicating that a bylaw violation may have occurred, and that the covered athletic association has determined that an investigation is warranted. The notice shall include, to the extent such information is available, the following:\n**(A)**\nEach program under investigation.\n**(B)**\nAll persons under investigation.\n**(C)**\nThe specific alleged violations under investigation including any sources relief on by the covered athletics association, whether verbal or written.\n**(D)**\nEach date or time period an alleged violation may have occurred.\n**(E)**\nThe rights and resources available to the accused party or parties.\n**(2)**\nThe notice under paragraph (1)(C) shall be limited to possible violations occurring not earlier than 2 years before the date the notice is provided to the member institution. The covered athletic association shall thereafter promptly notify the member institution of any other relevant information discovered in the course of the investigation.\n**(3)**\nPrior to commencing any enforcement proceeding, the covered athletic association shall provide the member institution with a notice of allegations not later than 8 months after the notice of inquiry is received under paragraph (1), which shall include the following:\n**(A)**\nDetails about each allegation.\n**(B)**\nThe potential penalties for each allegation.\n**(C)**\nThe information including any supporting evidence relief on to form the basis of the allegations\u201d between \u201cinformation and factors the covered athletic association considered in its determination to file charges.\n**(D)**\nThe rights and resources available to the member institution and involved individuals.\n**(4)**\nNot earlier than 60 days after the notice of allegations is received, there shall be a hearing before the covered athletic association\u2019s infractions committee or body with authorization to hear cases and prescribe punishments to member institutions which shall conform to the following requirements:\n**(A)**\nThe hearing shall commence not later than 1 year after the notice is provided under paragraph (1).\n**(B)**\nNo information from confidential sources may be offered into evidence or form the basis for any decision.\n**(5)**\nIn the event that there is any dispute regarding the covered athletic association\u2019s punishment of a member institution, the member institution may compel entry into arbitration conducted in accordance with the standard commercial arbitration rules of an established major national provider of arbitration and mediation services based in the United States, which will provide an independent review and binding decision. The arbitration shall be conducted by a three-person panel. The covered athletic association and member institution shall each appoint one arbitrator of their respective choosing. The third arbitrator shall be appointed in agreement by the two arbitrators appointed by each party.\n**(6)**\nThe covered athletic association shall conduct its enforcement proceedings and investigations in a fair and consistent manner, and the penalties issued against member institutions for bylaw infractions shall be equitable with respect to severity of the infraction and the member institution\u2019s history of infractions.\n**(7)**\nThe covered athletic association shall not disclose information relating to an ongoing investigation into a member institution until formal charges are filed in the notice of allegations submitted under paragraph (3). The member institution shall have discretionary authority to disclose any information relating to an ongoing investigation, and no information relating to an ongoing investigation shall be subject to any disclosure requirement under State law.\n##### (b) Report\nA covered athletic association shall submit an annual report to the Attorney General summarizing its enforcement proceedings, investigations, and issuance of punishments to member organizations under this Act over the preceding year. A covered athletic association shall submit an annual report to each State Attorney General (and the Attorney General for the District of Columbia) summarizing its enforcement proceedings, investigations, and issuance of punishments to member institutions headquartered in the State. Section 552 of title 5, United States Code, and any similar provision of State law does not apply to such report.\n#### 3. Limitation\nThe privileges of membership of any member institution in the covered athletic association may not be impaired as a consequence of any rights granted under this Act. Additionally, nothing herein shall be deemed to grant to the covered athletic association or any member institution any rights against a person or individual which it does not otherwise have.\n#### 4. Enforcement\n##### (a) Procedures\nThe Attorney General shall establish procedures\u2014\n**(1)**\nfor individuals and entities to file written, signed complaints respecting potential violations of this Act by a covered athletic association or any person acting as an agent thereof;\n**(2)**\nfor the investigation of those complaints which have probable validity;\n**(3)**\nfor the investigation of such other violations of this Act as the Attorney General determines to be appropriate; and\n**(4)**\nfor the evaluation of a covered athletic association\u2019s annual report to determine compliance with this Act.\n##### (b) Investigations and hearings\nIn conducting investigations and hearings pursuant to this section, the following shall apply:\n**(1)**\nAny hearing so requested shall be conducted before an administrative law judge of the Department of Justice determined by the Attorney General. The hearing shall be conducted in accordance with the requirements of section 554 of title 5, United States Code. The hearing shall be held at the nearest practicable place to the place where the person or covered athletic association resides or of the place where the alleged violation occurred. If no hearing is so requested, the Attorney General's imposition of the order shall constitute a final and unappealable order.\n**(2)**\nOfficers and employees of the Department of Justice (including the administrative law judges referred to in paragraph (1)) shall have reasonable access to examine evidence of any person or covered athletic association being investigated.\n**(3)**\nIf the administrative law judge determines, upon the preponderance of the evidence received, that a person or covered athletic association named in the complaint has violated the statute, the administrative law judge shall state his or her findings of fact and issue and cause to be served on such person or covered athletic association an order as follows:\n**(A)**\nThe administrative law judge shall order the person or covered athletic association to cease and desist from such violations and to pay a civil penalty in an amount of not less than $10,000 and not more than $15,000,000.\n**(B)**\nIn determining the amount of the penalty, due consideration shall be given to the good faith of the covered athletic association or person, the seriousness of the violation, and the history of previous violations.\n**(C)**\nThe administrative law judge may order the permanent removal of any member of the covered athletic association\u2019s governing body in the case of a violation, with due consideration for the good faith of the covered athletic association or person, the seriousness of the violation, and the history of previous violations.\n**(4)**\nThe Attorney General may, not earlier than 30 days after providing notice thereof to the person or covered athletic association, commence a hearing before an administrative law judge of the Department of Justice for any alleged violation of this Act by that person or covered athletic association. The administrative law judge may impose a civil penalty for any violation determined to have occurred.\n**(5)**\nAdministrative law judges may, if necessary, compel by subpoena the attendance of witnesses and the production of evidence at any designated place or hearing case of contumacy or refusal to obey a subpoena lawfully issued under this paragraph and upon application of the Attorney General, an appropriate district court of the United States may issue an order requiring compliance with such subpoena and any failure to obey such order may be punished by such court as a contempt thereof.\n**(6)**\nThe decision and order of an administrative law judge shall become the final agency decision and order of the Attorney General unless, within 30 days after the administrative law judge issues such order, the Attorney General modifies or vacates the decision and order, in which case the decision and order of the Attorney General shall become a final order under this subsection.\n**(7)**\nA person or covered athletic association adversely affected by a final order under this section may, within 45 days after the date the final order is issued, file a petition in the Court of Appeals for the appropriate circuit for review of the order.\n#### 5. Definitions\nIn this Act:\n**(1) Covered athletic association**\nThe term covered athletic association means an interstate athletic association, conference, or other organization with authority over intercollegiate athletics or that administers intercollegiate athletics, with at least 900 member institutions.\n**(2) Member institution**\nThe term member institution means an institution of higher education that maintains at least one intercollegiate athletic program that is a member of a covered athletic association.\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n#### 6. Effective date\nA covered athletic association shall carry out the requirements of this Act by not later than 1 year after the date of enactment of this Act.",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NCAA Accountability Act of 2025",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2025-07-09T15:11:22Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3976ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NCAA Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NCAA Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish due process requirements for the investigation of intercollegiate athletics, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T04:48:27Z"
    }
  ]
}
```
