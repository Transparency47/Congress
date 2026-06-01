# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/102?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/102
- Title: ROOMIE Act
- Congress: 119
- Bill type: S
- Bill number: 102
- Origin chamber: Senate
- Introduced date: 2025-01-15
- Update date: 2025-06-27T20:30:28Z
- Update date including text: 2025-06-27T20:30:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in Senate
- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-15: Introduced in Senate

## Actions

- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/102",
    "number": "102",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "ROOMIE Act",
    "type": "S",
    "updateDate": "2025-06-27T20:30:28Z",
    "updateDateIncludingText": "2025-06-27T20:30:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T20:13:56Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s102is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 102\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2025 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require Federal agencies to impose in-person work requirements for employees of those agencies and to occupy a certain portion of the office space of those agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reinforce Occupancy Obligations for Maximized Interagency Efficiency Act or the ROOMIE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of General Services.\n**(2) Federal agency**\nThe term Federal agency has the meaning given the term in section 621 of title 40, United States Code.\n**(3) Federal civilian real property**\nThe term Federal civilian real property has the meaning given the term in section 3 of the Federal Assets Sale and Transfer Act of 2016 ( 40 U.S.C. 1303 note; Public Law 114\u2013287 ).\n**(4) Usable square feet**\nThe term usable square feet has the meaning given the term by the Administrator.\n#### 3. Findings\nCongress finds that\u2014\n**(1)**\naccording to a 2023 review of Federal agencies by the Government Accountability Office\u2014\n**(A)**\n17 Federal agencies used on average an estimated 25 percent or less of the capacity of their headquarters buildings ; and\n**(B)**\n1 Federal agency headquarters examined would only occupy 67 percent of the office space of the Federal agency if 100 percent of the employees of the Federal agency worked in-person;\n**(2)**\naccording to a 2024 report by the Public Buildings Reform Board established by section 4(a) of the Federal Assets Sale and Transfer Act of 2016 ( 40 U.S.C. 1303 note; Public Law 114\u2013287 )\u2014\n**(A)**\nin the National Capital Region, the Federal Government owns or leases almost 90,000,000 square feet of property;\n**(B)**\na sample of Federal properties in Washington, D.C., maintained only 12 percent capacity on average;\n**(C)**\nbillions of dollars are being expended on buildings that should be disposed of given the new normal of low occupancy ; and\n**(D)**\nsome Federal agencies have developed cultural expectations that they should retain a flagship property despite significant under usage of that property; and\n**(3)**\naccording to a 2023 report by the Office of Audits of the Office of Inspector General of the General Services Administration\u2014\n**(A)**\nFederal Government buildings can pose significant health risks if they remain underutilized; and\n**(B)**\nsince July 2023, elevated levels of Legionella , which is a bacterium that can cause serious infection and death, were found in six GSA-controlled buildings, all of which are open to the public .\n#### 4. In-person work requirements\n##### (a) Federal agency policy modification\n**(1) In general**\nNot later than 120 days after the date of enactment of this Act, the head of each Federal agency shall amend the policies of the Federal agency, if necessary, to require\u2014\n**(A)**\nnot less than 80 percent of the employees of the Federal agency to work in-person Monday through Friday of each week, not including any day that is a legal public holiday described in section 6103 of title 5, United States Code, as certified by the Director of the Office of Personnel Management; and\n**(B)**\nexcept as provided in paragraph (2), not less than 60 percent of the usable square feet of the office space of the Federal agency in any Federal civilian real property owned, leased, or controlled by the Federal agency to be occupied by employees of the Federal agency, as certified by the Administrator.\n**(2) Exception**\n**(A) In general**\nIf a Federal agency does not employ enough individuals to occupy 60 percent of the usable square feet of the office space of the Federal agency in any Federal civilian real property owned, leased, or controlled by the Federal agency, the head of the Federal agency shall, not later than 1 year after the date of enactment of this Act, prepare and submit to the Administrator, the Committee on Environment and Public Works of the Senate, and the Committee on Transportation and Infrastructure of the House of Representatives an occupancy plan in accordance with subparagraph (B).\n**(B) Requirements**\nAn occupancy plan prepared and submitted under subparagraph (A) shall detail how the Federal agency plans to reach 60 percent occupancy in the usable square feet of the office space of the Federal agency in any Federal civilian real property owned, leased, or controlled by the Federal agency through the use of individuals employed by any Federal agency, with special consideration given to individuals employed by different Federal agencies.\n##### (b) Report\nNot later than 1 year after the date that is 120 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report regarding the implementation of the requirement under subsection (a)(1), as certified by the Director of the Office of Personnel Management and the Administrator, as applicable.\n#### 5. Noncompliance\n##### (a) In general\nIf a Federal agency fails to comply with section 4(a) by the deadlines described in that section, the Federal agency or the General Services Administration, as applicable, shall sell, terminate, or be prohibited from re-signing the lease for, the applicable Federal civilian real property in accordance with subsection (b) or (c), as applicable.\n##### (b) Property owned or controlled by the Federal agency\nIf the Federal agency owns or controls the Federal civilian real property in which the office space described in subsection (a) is located, the Federal agency or the General Services Administration, as applicable, shall sell the Federal civilian real property.\n##### (c) Property leased by the Federal agency\nIf the Federal agency leases the Federal civilian real property in which the office space described in subsection (a) is located, the Federal agency or the General Services Administration, as applicable\u2014\n**(1)**\nif the lease contains an early termination or other applicable provision\u2014\n**(A)**\nshall execute that provision and terminate the lease early; and\n**(B)**\nshall not re-sign the lease; or\n**(2)**\nif the lease does not contain an early termination or other applicable provision, shall not re-sign the lease.",
      "versionDate": "2025-01-15",
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
            "name": "Congressional oversight",
            "updateDate": "2025-02-19T21:26:24Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-19T21:26:19Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-19T21:26:14Z"
          },
          {
            "name": "Lease and rental services",
            "updateDate": "2025-02-19T21:26:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-15T14:47:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119s102",
          "measure-number": "102",
          "measure-type": "s",
          "orig-publish-date": "2025-01-15",
          "originChamber": "SENATE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s102v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Reinforce Occupancy Obligations for Maximized Interagency Efficiency Act or the ROOMIE Act</strong></p><p>This bill establishes occupancy requirements for federal office buildings and directs agencies to sell or terminate leases on unused office space.\u00a0</p><p>The bill directs agencies to amend their policies within 120 days of the bill's enactment to require not less than 80%\u00a0of the agency's employees to work on site. The policies must also ensure that at least\u00a060% of the usable square feet of the agency's office space is occupied by agency employees.\u00a0 </p><p>Agencies that do not employ enough individuals to occupy 60%\u00a0of the agency's office space must provide an occupancy plan to the General Services Administration and Congress detailing how it will meet that goal, particularly by working with other federal agencies. The plan must be submitted within one year of the bill's enactment.</p><p>The Government Accountability Office must report to Congress regarding agencies' compliance with these requirements.</p><p>Agencies that do not comply with these requirements must sell their properties, terminate leases, or not renew leases, as applicable.</p><p></p>"
        },
        "title": "ROOMIE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s102.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reinforce Occupancy Obligations for Maximized Interagency Efficiency Act or the ROOMIE Act</strong></p><p>This bill establishes occupancy requirements for federal office buildings and directs agencies to sell or terminate leases on unused office space.\u00a0</p><p>The bill directs agencies to amend their policies within 120 days of the bill's enactment to require not less than 80%\u00a0of the agency's employees to work on site. The policies must also ensure that at least\u00a060% of the usable square feet of the agency's office space is occupied by agency employees.\u00a0 </p><p>Agencies that do not employ enough individuals to occupy 60%\u00a0of the agency's office space must provide an occupancy plan to the General Services Administration and Congress detailing how it will meet that goal, particularly by working with other federal agencies. The plan must be submitted within one year of the bill's enactment.</p><p>The Government Accountability Office must report to Congress regarding agencies' compliance with these requirements.</p><p>Agencies that do not comply with these requirements must sell their properties, terminate leases, or not renew leases, as applicable.</p><p></p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s102"
    },
    "title": "ROOMIE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reinforce Occupancy Obligations for Maximized Interagency Efficiency Act or the ROOMIE Act</strong></p><p>This bill establishes occupancy requirements for federal office buildings and directs agencies to sell or terminate leases on unused office space.\u00a0</p><p>The bill directs agencies to amend their policies within 120 days of the bill's enactment to require not less than 80%\u00a0of the agency's employees to work on site. The policies must also ensure that at least\u00a060% of the usable square feet of the agency's office space is occupied by agency employees.\u00a0 </p><p>Agencies that do not employ enough individuals to occupy 60%\u00a0of the agency's office space must provide an occupancy plan to the General Services Administration and Congress detailing how it will meet that goal, particularly by working with other federal agencies. The plan must be submitted within one year of the bill's enactment.</p><p>The Government Accountability Office must report to Congress regarding agencies' compliance with these requirements.</p><p>Agencies that do not comply with these requirements must sell their properties, terminate leases, or not renew leases, as applicable.</p><p></p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s102"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s102is.xml"
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
      "title": "ROOMIE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ROOMIE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reinforce Occupancy Obligations for Maximized Interagency Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require Federal agencies to impose in-person work requirements for employees of those agencies and to occupy a certain portion of the office space of those agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T03:03:24Z"
    }
  ]
}
```
