# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1269?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1269
- Title: Promoting United States Leadership in Standards Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1269
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2026-05-21T20:42:35Z
- Update date including text: 2026-05-21T20:42:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1269",
    "number": "1269",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Promoting United States Leadership in Standards Act of 2025",
    "type": "S",
    "updateDate": "2026-05-21T20:42:35Z",
    "updateDateIncludingText": "2026-05-21T20:42:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
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
        "item": {
          "date": "2026-03-19T14:00:14Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-02T22:36:32Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1269is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1269\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mrs. Blackburn (for herself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo promote United States leadership in technical standards by directing the National Institute of Standards and Technology and the Department of State to take certain actions to encourage and enable United States participation in developing standards and specifications for artificial intelligence and other critical and emerging technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting United States Leadership in Standards Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Artificial intelligence and other critical and emerging technologies**\nThe term artificial intelligence and other critical and emerging technologies means a subset of artificial intelligence and other critical and emerging technologies included in the list of such technologies identified and maintained by the National Science and Technology Council of the Office of Science and Technology Policy as the Director considers appropriate for purposes of this Act.\n**(2) Director**\nThe term Director means the Director of the National Institute of Standards and Technology.\n#### 3. United States participation in organizations developing standards and specifications for artificial intelligence and other critical and emerging technologies\n##### (a) Briefing required\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Director shall, in coordination with the Secretary of State, provide to Congress a briefing to assist in the evaluation and identification of opportunities for Federal Government support for industry-led efforts in the development of technical standards for artificial intelligence and other critical and emerging technologies.\n**(2) Interagency consultation**\nIn preparing the briefing required by paragraph (1), the Director and the Secretary of State shall jointly consult with the heads of such Federal agencies as they jointly consider relevant.\n**(3) Elements**\nThe briefing provided pursuant to paragraph (1) shall include the following:\n**(A)**\nAn overview of standards activities relating to artificial intelligence and other critical and emerging technologies and information about the following:\n**(i)**\nKey technical standards that are the subject of ongoing activity.\n**(ii)**\nKey standards bodies hosting these activities.\n**(iii)**\nAny Federal agency that is participating in these activities.\n**(B)**\nAn analysis identifying where participation by United States industry and Federal agencies in standards activities in artificial intelligence and other critical and emerging technologies would be facilitated or enhanced by conducting standards meetings hosted in the United States.\n**(C)**\nRecommendations for effectively informing United States industry and Federal agencies on ongoing standardization activities with the objective of increasing participation of such industry and agencies in such activities.\n**(4) Federal agency notice requirement**\n**(A) In general**\nUsing the mechanism established pursuant to subparagraph (B), each head of a Federal agency shall transmit to the Secretary of State and the Director notice of the participation of their respective Federal agency in a standards activity relating to artificial intelligence and other critical and emerging technologies.\n**(B) Mechanism**\nThe Secretary of State and the Director shall, in coordination with the Director of the Office of Management and Budget, jointly develop a mechanism for reporting participation by Federal agencies in standards activities.\n##### (b) Web portal\n**(1) In general**\nIn order to inform United States industry and Federal agencies about existing and ongoing international efforts to develop technical standards for artificial intelligence and other critical and emerging technologies and opportunities for participation in such efforts, the Director shall, in coordination with the Secretary of State, establish an accessible web portal to help such industry and agencies navigate and participate in such efforts.\n**(2) Contents**\nThe web portal established pursuant to paragraph (1) shall include regularly updated lists of the following:\n**(A)**\nInternational efforts described in paragraph (1) and information on opportunities for participation in such efforts.\n**(B)**\nInformation on accessing standards, both in development and published, for artificial intelligence and other critical and emerging technologies.\n**(3) Administration**\nThe Director may, in coordination with the Secretary of State, enter into such cooperative agreements with such nongovernmental organizations as the Director considers appropriate to establish the web portal required by paragraph (1).\n#### 4. Pilot program to support standards meetings for artificial intelligence and other critical and emerging technologies in the United States\n##### (a) Pilot program required\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and subject to the availability of appropriated funds, the Director shall, in coordination with the Secretary of State and the heads of such other Federal agencies as the Director considers appropriate, establish a pilot program on supporting standards meetings for artificial intelligence and other critical and emerging technologies in the United States by awarding grants to eligible entities described in subsection (b) hosting meetings of organizations described in paragraph (1) of such subsection to support the hosting of such meetings in the United States.\n**(2) Administration**\nThe Director may, in coordination with the Secretary of State, carry out the pilot program required by paragraph (1) by entering into such cooperative agreements with such nongovernmental organizations as the Director considers appropriate to establish and administer the pilot program.\n##### (b) Eligible entities\nFor purposes of the pilot program required by subsection (a), an eligible entity is\u2014\n**(1)**\nan organization that is developing standards and specifications for artificial intelligence and other critical and emerging technologies for at least 1 technical standard that affects the interests of 1 or more Federal agencies; or\n**(2)**\nan entity that hosts an organization described in paragraph (1).\n##### (c) Grants\n**(1) In general**\nIn carrying out the pilot program required by subsection (a), the Director shall, in coordination with the Secretary of State, award grants to eligible entities to host meetings as described in such subsection.\n**(2) Use of funds**\nAn eligible entity receiving a grant under this subsection to host a meeting in the United States may use the amount of the grant for such costs as the Director considers reasonable for hosting the meeting in the United States, but not more than fifty percent of anticipated cost of hosting the meeting and not more than a maximum amount that the Director shall establish for purposes of this subsection. Such costs may include the following:\n**(A)**\nCosts related to the preparation and planning of meetings described in subsection (a).\n**(B)**\nMeeting venue-related expenses.\n**(C)**\nSuch other costs that may support the eligible entity in conducting a standards meeting in the United States.\n**(3) Considerations**\nIn deciding whether to award a grant under this subsection to an eligible entity to host a meeting, the Director may, in coordination with the Secretary of State, consider the extent to which the eligible entity\u2014\n**(A)**\nis or hosts an organization that administers technical standards activity in artificial intelligence and other critical and emerging technologies that involves United States-based participants, including but not limited to participants from Federal agencies of the United States;\n**(B)**\nhas a demonstrable history of participating in or hosting successful meetings; and\n**(C)**\nhas a stable or growing participant base.\n##### (d) Guidance\n**(1) In general**\nThe Director shall, in coordination with the Secretary of State, develop and periodically update guidance for the pilot program carried out under this section.\n**(2) Elements**\nThe guidance developed and updated pursuant to paragraph (1) shall cover the following:\n**(A)**\nEligibility for grants awarded under the pilot program.\n**(B)**\nHow grants are awarded under subsection (c).\n**(C)**\nThe duration and amounts of grants awarded under subsection (c).\n**(D)**\nThe merit review process for the pilot program.\n**(E)**\nPriority areas for technical standards activity.\n**(F)**\nMeans for recipients of grants under the pilot program to report expenses relating to costs described in subsection (c)(2)(D).\n**(G)**\nSuch additional matters as the Director determines appropriate for purposes of the pilot program.\n##### (e) Briefings for congress\n**(1) In general**\nDuring the third year of the pilot program carried out under this section and in each subsequent year of the pilot program, the Director and the Secretary of State shall jointly provide Congress with a briefing on the pilot program.\n**(2) Elements**\nEach briefing provided pursuant to paragraph (1) shall include the following:\n**(A)**\nAn assessment of the effectiveness of the pilot program with respect to improving the hosting of standards meetings in the United States.\n**(B)**\nIdentification of the recipients of grants under the pilot program.\n**(C)**\nThe geographic distribution of attendees at meetings supported with grants under the pilot program.\n**(D)**\nA summary of the expenses for which the amounts of grants awarded under the pilot program were used.\n##### (f) Recommendations for permanent implementation\nIf, before the date that is 2 years after the date of the enactment of this Act, the Director determines, in consultation with the Secretary of State, that providing support as described in subsection (a) is feasible and advisable, the Director shall, not later than 2 years after the date of the enactment of this Act\u2014\n**(1)**\ndevelop recommendations for such legislative or administrative action as the Director considers appropriate to establish a permanent implementation of the pilot program; and\n**(2)**\nsubmit to Congress the recommendations developed pursuant to paragraph (1).\n##### (g) Termination\nThe pilot program required by subsection (a)(1) shall terminate on the date that is 5 years after the date of the enactment of this Act.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000 for the period of fiscal years 2024 through 2028.",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-04-27",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Energy and Commerce, Agriculture, Oversight and Government Reform, Education and Workforce, the Judiciary, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8516",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Leadership in AI Act",
      "type": "HR"
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-03-30T15:57:34Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-03-30T15:57:34Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-03-30T15:57:34Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2026-03-30T15:57:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-02T13:24:45Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1269is.xml"
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
      "title": "Promoting United States Leadership in Standards Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting United States Leadership in Standards Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote United States leadership in technical standards by directing the National Institute of Standards and Technology and the Department of State to take certain actions to encourage and enable United States participation in developing standards and specifications for artificial intelligence and other critical and emerging technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:53Z"
    }
  ]
}
```
