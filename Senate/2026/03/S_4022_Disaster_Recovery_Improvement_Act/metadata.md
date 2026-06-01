# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4022?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4022
- Title: Disaster Recovery Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 4022
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-30T22:30:57Z
- Update date including text: 2026-03-30T22:30:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4022",
    "number": "4022",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Disaster Recovery Improvement Act",
    "type": "S",
    "updateDate": "2026-03-30T22:30:57Z",
    "updateDateIncludingText": "2026-03-30T22:30:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T21:12:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4022is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4022\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Budd (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish an interagency task force on expediting disaster relief funding, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Recovery Improvement Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nNumerous programs administered by Federal agencies, while not dedicated exclusively to disaster recovery, play a critical role in supporting and expediting recovery efforts.\n**(2)**\nThe delayed delivery of Federal disaster relief funding to local communities in the wake of recent natural disasters, including Hurricane Helene, revealed new and longstanding bottlenecks in Federal disaster response.\n**(3)**\nState and local governments should have greater input in how the Federal Government administers disaster relief assistance and responsibility for responding to natural disasters.\n##### (b) Sense of Congress\nIt is the sense of Congress that Federal agencies must incorporate recommendations from State and local governments to improve their disaster response capability.\n#### 3. Disaster Recovery Improvement Task Force\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall establish an interagency task force on expediting disaster relief funding to be known as the Disaster Recovery Improvement Task Force .\n##### (b) Membership\n**(1) In general**\nThe interagency task force established under subsection (a), shall consist of\u2014\n**(A)**\na senior official from the Federal Emergency Management Agency, appointed by the Administrator of the Federal Emergency Management Agency, to serve as chair;\n**(B)**\na senior official, appointed by the head of the respective agency of the official, experienced in handling disaster recovery matters from each of\u2014\n**(i)**\nthe Small Business Administration;\n**(ii)**\nthe Department of Housing and Urban Development;\n**(iii)**\nthe Department of Agriculture;\n**(iv)**\nthe Department of Health and Human Services;\n**(v)**\nthe Department of Labor;\n**(vi)**\nthe Department of Transportation;\n**(vii)**\nthe Department of Commerce;\n**(viii)**\nthe Department of the Treasury;\n**(ix)**\nthe Department of the Interior;\n**(x)**\nthe Environmental Protection Agency;\n**(xi)**\nthe Army Corp of Engineers; and\n**(xii)**\nthe Office of Management and Budget;\n**(C)**\n4 state governors, jointly appointed by the Chairs and Ranking Members of the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives , representing States that, during the 3-year period immediately preceding appointment to the interagency task force, have experienced a major disaster, as defined in section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ), of which\u2014\n**(i)**\n1 was a hurricane;\n**(ii)**\n1 was a wildfire;\n**(iii)**\n1 was a tornado; and\n**(iv)**\n1 was an earthquake; and\n**(D)**\n4 county commissioners, jointly appointed by the Chairs and Ranking Members of the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives , representing a county in a State that, during the 3-year period immediately preceding appointment to the interagency task force, have experienced a major disaster, as defined in section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ), of which\u2014\n**(i)**\n1 was a hurricane;\n**(ii)**\n1 was a wildfire;\n**(iii)**\n1 was a tornado; and\n**(iv)**\n1 was an earthquake.\n**(2) Advisory members**\nMembers of Congress representing the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives may serve on the interagency task force established under subsection (a) as advisory members in a non-voting capacity.\n##### (c) Reports\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the interagency task force established under subsection (a) shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate , the Committee on Transportation and Infrastructure of the House of Representatives , and the Committee on Homeland Security of the House of Representatives and make publicly available a report that\u2014\n**(A)**\nidentifies the programs, including temporary programs, for which Congress appropriates funds to aid recovery purposes relating to the consequences of natural disasters;\n**(B)**\ncontains recommendations for Federal agencies on the most effective way to expedite disaster relief efforts, including recommendations to\u2014\n**(i)**\nstreamline the establishment and administration of temporary programs;\n**(ii)**\nimprove the timeliness, accessibility, and clarity of applications for funding; and\n**(iii)**\nreduce delays in the review and obligation of funds with respect to applications received;\n**(C)**\nidentifies the different types of funding mechanisms for which Congress provides appropriations to Federal agencies for disaster relief, including grants, loans, reimbursements, and contract authority;\n**(D)**\ncontains recommendations to Federal agencies and Congress on the most effective way to expedite the expenditure of the funds identified under subparagraph (C) toward disaster relief;\n**(E)**\ncontains recommendations for Federal agencies and Congress to strengthen State capacity to prepare for, respond to, and recover from natural disasters;\n**(F)**\nidentifies factors that cause delays in disaster relief program funding being made available or obligated, including during transitions from one presidential administration to another presidential administration;\n**(G)**\nincludes recommendations on how outgoing and incoming Presidential administrations can equip themselves to set up and deliver disaster relief aid without delay, including an assessment of actions required of both outgoing and incoming Presidential administrations to ensure continuity and uninterrupted delivery of disaster relief funding;\n**(H)**\nevaluates barriers within Federal agencies and across Federal agencies that delay the obligation or expenditure of disaster relief funds and provides recommendations to address those barriers; and\n**(I)**\nassesses specific actions taken by Federal agencies over time that have improved or hindered interagency coordination, State and local engagement, and the timely delivery of disaster relief funding.\n**(2) Recommendations**\nIn making recommendations for the report under paragraph (1), the interagency task force shall make recommendations for ways to expedite making available and obligating specific funding appropriated by Congress to certain agencies, including\u2014\n**(A)**\nto the Federal Emergency Management Agency, including with respect to Public Assistance funding under section 406 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5172 ) and Hazard Mitigation Grant Program funding under section 404 of that Act ( 42 U.S.C. 5170 );\n**(B)**\nto the Department of Housing and Urban Development, including with respect to funding under the Community Development Block Grant Disaster Recovery program;\n**(C)**\nto the Department of Agriculture, including with respect to funding for necessary expenses relating to losses of revenue or quality or production of crops as a consequence of a major disaster, as defined in section 404 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 );\n**(D)**\nto the Department of Agriculture, including with respect to Forest Service operations, forest and rangeland research, state, private, and tribal forestry, and National Forest System funding for necessary expenses relating to the consequences of disaster relief;\n**(E)**\nto the Department of Labor, including with respect to Disaster Recovery Dislocated Worker Grant funding under section 170 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3225 );\n**(F)**\nto the Department of Commerce, including with respect to Economic Development Administration funding under the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3121 et seq. );\n**(G)**\nto the Department of the Interior, including with respect to National Park Service Historic Preservation Fund and construction funding for necessary expenses relating to the consequences of disaster relief; and\n**(H)**\nto the Environmental Protection Agency, including with respect to Clean Water State Revolving Fund funding under title VI of the Federal Water Pollution Control Act ( 33 U.S.C. 1381 et seq. ).\n**(3) Implementation report**\nNot later than 180 days after the date on which the interagency task force submits the report under paragraph (1), the interagency task force shall submit to the congressional committees described in that paragraph a report detailing\u2014\n**(A)**\nwhich of the recommendations contained in the report under paragraph (1) shall be implemented by Federal agencies and why those recommendations in the report not being implemented are not selected for implementation;\n**(B)**\nhow the recommendations selected for implementation will be carried out; and\n**(C)**\nlegislative recommendations for Congress to support the recommendations selected for implementation.\n##### (d) No additional funding\nNo additional funds are authorized to be appropriated to carry out this Act.\n##### (e) Termination\nThe interagency task force established under subsection (a) shall terminate on the date that is 90 days after the date on which the interagency task force submits the report under subsection (c)(3).",
      "versionDate": "2026-03-05",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Emergency Management",
        "updateDate": "2026-03-30T22:30:57Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4022is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an interagency task force on expediting disaster relief funding, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:32Z"
    },
    {
      "title": "Disaster Recovery Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Recovery Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
