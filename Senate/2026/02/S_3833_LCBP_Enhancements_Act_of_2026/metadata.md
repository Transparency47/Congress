# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3833?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3833
- Title: LCBP Enhancements Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3833
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-03-09T12:20:58Z
- Update date including text: 2026-03-09T12:20:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3833",
    "number": "3833",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "LCBP Enhancements Act of 2026",
    "type": "S",
    "updateDate": "2026-03-09T12:20:58Z",
    "updateDateIncludingText": "2026-03-09T12:20:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T20:02:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-02-11",
      "state": "VT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3833is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3833\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Welch (for himself, Mr. Schumer , Mr. Sanders , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Federal Water Pollution Control Act to provide for the selection of a fiscal agent for the Patrick Leahy Lake Champlain Basin Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Patrick Leahy Lake Champlain Basin Program Enhancements Act of 2026 or the LCBP Enhancements Act of 2026 .\n#### 2. Patrick Leahy Lake Champlain Basin Program\nSection 120 of the Federal Water Pollution Control Act ( 33 U.S.C. 1270 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)(A), by striking New England Interstate Water Pollution Control Commission and inserting fiscal agent ; and\n**(B)**\nby adding at the end the following:\n(3) Fiscal agent (A) In general The Steering Committee and the Administrator shall jointly select a qualified entity to serve as the fiscal agent for the Patrick Leahy Lake Champlain Basin Program. (B) Assessment (i) In general Beginning as soon as practicable after the date of enactment of the LCBP Enhancements Act of 2026 , and as necessary but not less frequently than once every 5 years thereafter, the Steering Committee and the Administrator shall jointly assess the effectiveness of the fiscal agent and, if appropriate, select a new qualified entity to serve as the fiscal agent through a competitive process. (ii) Stakeholder engagement In carrying out the assessments required under clause (i), the Steering Committee and the Administrator shall consult with, and incorporate feedback from, impacted stakeholders. (iii) No competitive process after selection On selection of a fiscal agent, the Administrator shall award funding to the fiscal agent without competition until such time as a new fiscal agent is selected. (iv) New fiscal agent selection If the Steering Committee and the Administrator jointly select a new fiscal agent pursuant to clause (i)\u2014 (I) the Administrator may de-obligate unobligated or unexpended funds from prior awards under clause (iii) and re-obligate those funds to the new fiscal agent; (II) the Steering Committee and the Administrator shall, to the maximum extent practicable, ensure the continuity of the staff, programming, funding awards, and other activities and administrative functions of the Patrick Leahy Lake Champlain Basin Program, as determined necessary by the Steering Committee and the Administrator; and (III) the Steering Committee and the Administrator shall, to the maximum extent practicable, ensure that the new fiscal agent\u2014 (aa) is headquartered in the Lake Champlain drainage basin; (bb) only if a suitable entity described in item (aa) is not identified, is headquartered in the State of New York or Vermont; or (cc) only if a suitable entity described in item (bb) is not identified, maintains a significant staffing presence, including staff that would have decisionmaking authority with respect to the Patrick Leahy Lake Champlain Basin Program, within the Lake Champlain drainage basin. (v) Report to Congress Not later than 90 days after the date on which an assessment under clause (i) is completed, the Administrator shall submit to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report that describes the findings of that assessment, including a description of the reasons for maintaining the current fiscal agent or selecting a new fiscal agent. (C) Responsibilities The responsibilities of the fiscal agent may include, as jointly determined appropriate by the Steering Committee and the Administrator, executing payroll, paying bills and fulfilling other obligations, developing and executing funding agreements, and acting as a fiduciary for the Patrick Leahy Lake Champlain Basin Program. ;\n**(2)**\nby redesignating subsections (g) through (i) as subsections (h) through (j), respectively;\n**(3)**\nby inserting after subsection (f) the following:\n(g) Great Lakes Fishery Commission (1) In general The United States Section of the Great Lakes Fishery Commission may undertake, fund, and support work on Lake Champlain, in the Lake Champlain drainage basin, and in other areas within the Saint Lawrence River basin in Vermont and New York, including through\u2014 (A) fisheries and aquatic ecosystem research, monitoring, restoration, and management; (B) sea lamprey control; (C) aquatic invasive species prevention and mitigation; (D) public engagement and education; and (E) other work to implement the Plan. (2) Authorization In carrying out paragraph (1), the United States Section of the Great Lakes Fishery Commission may work with the Patrick Leahy Lake Champlain Basin Program, Federal and State agencies, institutions of higher education, nonprofit organizations, units of local government, and Canadian federal and Quebec provincial authorities. ;\n**(4)**\nin subsection (h) (as so redesignated)\u2014\n**(A)**\nby redesignating paragraphs (1), (2), and (3) as paragraphs (3), (2), and (4), respectively, and moving the paragraphs so as to appear in numerical order;\n**(B)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) Fiscal agent The term fiscal agent means an organization, including a nonprofit organization, interstate commission, or other entity jointly determined appropriate by the Administrator and the Steering Committee, that provides fiscal and administrative management support for the Patrick Leahy Lake Champlain Basin Program under the direction of the Steering Committee and the Administrator. ; and\n**(C)**\nby adding at the end the following:\n(5) Steering Committee The term Steering Committee means the Steering Committee established by the Lake Champlain Management Conference on October 9, 1996, to implement the Lake Champlain Management Plan and maintained under the most recent Memorandum of Understanding on Environmental Cooperation on the Management of Lake Champlain entered into between the State of New York, the State of Vermont, and, if the Province of Quebec elects to participate, the Province of Quebec. ; and\n**(5)**\nin subsection (j) (as so redesignated), by striking 2027 and inserting 2032 .",
      "versionDate": "2026-02-11",
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
        "actionDate": "2026-02-12",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "7560",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LCBP Enhancements Act of 2026",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2026-03-02T18:14:17Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3833is.xml"
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
      "title": "LCBP Enhancements Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T03:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LCBP Enhancements Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Patrick Leahy Lake Champlain Basin Program Enhancements Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Water Pollution Control Act to provide for the selection of a fiscal agent for the Patrick Leahy Lake Champlain Basin Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T03:48:26Z"
    }
  ]
}
```
