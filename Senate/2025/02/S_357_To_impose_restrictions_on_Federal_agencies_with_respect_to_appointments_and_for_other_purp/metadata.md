# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/357
- Title: Federal Freeze Act
- Congress: 119
- Bill type: S
- Bill number: 357
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2026-04-20T15:47:56Z
- Update date including text: 2026-04-20T15:47:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/357",
    "number": "357",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Federal Freeze Act",
    "type": "S",
    "updateDate": "2026-04-20T15:47:56Z",
    "updateDateIncludingText": "2026-04-20T15:47:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
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
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T20:42:27Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s357is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 357\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo impose restrictions on Federal agencies with respect to appointments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Freeze Act .\n#### 2. Freeze on Federal hiring and salaries\n##### (a) Definitions\nIn this section:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Baseline number**\nThe term baseline number means, with respect to an agency, the number of employees employed by the agency (including individuals occupying full-time equivalent positions in the agency), as of the date of enactment of this Act.\n**(3) Employee**\nThe term employee means an employee of an agency.\n##### (b) General prohibitions\nNotwithstanding any other provision of law or regulation, during the 1-year period beginning on the date of enactment of this Act, the following shall apply:\n**(1)**\n**(A)**\nExcept as provided in subparagraph (B), the head of an agency may not increase the number of employees employed by the agency beyond the baseline number.\n**(B)**\nDuring the 1-year period beginning on the date of enactment of this Act, the head of an agency may appoint an individual to a position within the agency, even if appointing that individual would increase the number of employees employed by the agency beyond the baseline number, if the agency head determines that\u2014\n**(i)**\nmaking that appointment serves the interest of law enforcement, public safety, or the national security of the United States; or\n**(ii)**\nthe individual so appointed is essential to respond to an emergency declared under section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5191 ).\n**(2)**\nThe annual rate of basic pay of an employee, as in effect on the date of enactment of this Act, may not be increased.\n##### (c) Reduction in force\n**(1) In general**\nSubject to paragraph (2), the head of each agency shall take such measures, without regard to any other provision of law or regulation, to ensure that\u2014\n**(A)**\nas of the date that is 2 years after the date of enactment of this Act, the number of employees employed by the agency is 2 percent less than the baseline number; and\n**(B)**\nas of the date that is 3 years after the date of enactment of this Act, the number of employees employed by the agency is 5 percent less than the baseline number.\n**(2) Exemption**\nAn employee who the head of the employing agency determines serves the interest of law enforcement, public safety, or the national security of the United States, or who is essential to respond to an emergency declared under section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5191 ) (as determined by that agency head), shall not apply for the purposes of determining the number of employees employed by that agency under subparagraph (A) or (B) of paragraph (1).",
      "versionDate": "2025-02-03",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "200",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Federal Freeze Act",
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
            "name": "Employee hiring",
            "updateDate": "2025-06-20T18:48:17Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-20T18:48:21Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-06-20T18:48:25Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-20T18:48:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-05T15:33:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-03",
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
          "measure-id": "id119s357",
          "measure-number": "357",
          "measure-type": "s",
          "orig-publish-date": "2025-02-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s357v00",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-02-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Federal Freeze Act</strong></p><p>This bill bars pay raises for federal employees for one year and requires reductions in the number of employees at each federal agency.</p><p>The bill prohibits agencies from increasing the basic pay of any employee for one year after enactment. Also in that first year, the bill prohibits each federal agency from increasing the number of its employees beyond the number employed on the date of the bill's enactment, except that the agency may increase such number (1) when making appointments to positions related to law enforcement, public safety, or national security; or (2) if the individual so appointed is essential to emergency response under the Stafford Act. (The Stafford Act authorizes the President to issue declarations that provide states, tribes, and localities with a range of federal assistance in response to natural disasters and man-made incidents).</p><p>Additionally, the bill requires reductions in force such that within three years of the bill's enactment the number of employees at each agency is 5% lower than it was on the date of the bill's enactment. Employees that serve the interest of law enforcement, public safety, or national security or are essential to emergency response under the Stafford Act are not counted for the purposes of determining the number of employees at each agency.</p>"
        },
        "title": "Federal Freeze Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s357.xml",
    "summary": {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Freeze Act</strong></p><p>This bill bars pay raises for federal employees for one year and requires reductions in the number of employees at each federal agency.</p><p>The bill prohibits agencies from increasing the basic pay of any employee for one year after enactment. Also in that first year, the bill prohibits each federal agency from increasing the number of its employees beyond the number employed on the date of the bill's enactment, except that the agency may increase such number (1) when making appointments to positions related to law enforcement, public safety, or national security; or (2) if the individual so appointed is essential to emergency response under the Stafford Act. (The Stafford Act authorizes the President to issue declarations that provide states, tribes, and localities with a range of federal assistance in response to natural disasters and man-made incidents).</p><p>Additionally, the bill requires reductions in force such that within three years of the bill's enactment the number of employees at each agency is 5% lower than it was on the date of the bill's enactment. Employees that serve the interest of law enforcement, public safety, or national security or are essential to emergency response under the Stafford Act are not counted for the purposes of determining the number of employees at each agency.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s357"
    },
    "title": "Federal Freeze Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Freeze Act</strong></p><p>This bill bars pay raises for federal employees for one year and requires reductions in the number of employees at each federal agency.</p><p>The bill prohibits agencies from increasing the basic pay of any employee for one year after enactment. Also in that first year, the bill prohibits each federal agency from increasing the number of its employees beyond the number employed on the date of the bill's enactment, except that the agency may increase such number (1) when making appointments to positions related to law enforcement, public safety, or national security; or (2) if the individual so appointed is essential to emergency response under the Stafford Act. (The Stafford Act authorizes the President to issue declarations that provide states, tribes, and localities with a range of federal assistance in response to natural disasters and man-made incidents).</p><p>Additionally, the bill requires reductions in force such that within three years of the bill's enactment the number of employees at each agency is 5% lower than it was on the date of the bill's enactment. Employees that serve the interest of law enforcement, public safety, or national security or are essential to emergency response under the Stafford Act are not counted for the purposes of determining the number of employees at each agency.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s357"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s357is.xml"
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
      "title": "Federal Freeze Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Freeze Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose restrictions on Federal agencies with respect to appointments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:26Z"
    }
  ]
}
```
