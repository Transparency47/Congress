# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/866?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/866
- Title: Accelerating Broadband Permits Act
- Congress: 119
- Bill type: S
- Bill number: 866
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-07-14T17:50:54Z
- Update date including text: 2025-07-14T17:50:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S1581)
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S1581)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/866",
    "number": "866",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Accelerating Broadband Permits Act",
    "type": "S",
    "updateDate": "2025-07-14T17:50:54Z",
    "updateDateIncludingText": "2025-07-14T17:50:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S1581)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T20:33:24Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s866is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 866\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Thune (for himself, Mr. Luj\u00e1n , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require executive agencies to take steps to better meet the statutory deadline for processing communications use applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating Broadband Permits Act .\n#### 2. Tracking and improving processing times for communications use applications\nSection 6409(b)(3) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(b)(3) ) is amended by adding at the end the following:\n(E) Tracking and improving processing times (i) Data controls An executive agency shall develop controls to ensure that data is sufficiently accurate and complete to track the processing time for each application described in subparagraph (A). (ii) Requirement to analyze, address, and report on delay factors With respect to the factors that contribute to delays in processing applications described in subparagraph (A), an executive agency shall\u2014 (I) analyze the factors as the delays are occurring; (II) take actions to address the factors; and (III) provide an annual report on the factors to\u2014 (aa) the Committee on Commerce, Science, and Transportation of the Senate; (bb) the Committee on Energy and Natural Resources of the Senate; (cc) the Committee on Energy and Commerce of the House of Representatives; (dd) the Committee on Natural Resources of the House of Representatives; and (ee) each committee of Congress with jurisdiction over the executive agency. (iii) Method for alerting staff to at-risk applications An executive agency shall establish a method to alert employees of the executive agency to any application described in subparagraph (A) with respect to which the executive agency is at risk of failing to meet the 270-day deadline under that subparagraph. .\n#### 3. Minimum broadband project cost\nSection 41001(6)(A) of the FAST Act ( 42 U.S.C. 4370m(6)(A) ) is amended\u2014\n**(1)**\nin clause (iii), by striking or at the end;\n**(2)**\nby redesignating clause (iv) as clause (v); and\n**(3)**\nby inserting after clause (iii) the following:\n(iv) (I) is subject to NEPA; (II) involves the construction of infrastructure for broadband; and (III) is likely to require a total investment of more than $5,000,000; or .",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-03-12",
        "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably."
      },
      "number": "323",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PLAN for Broadband Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-28T11:55:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119s866",
          "measure-number": "866",
          "measure-type": "s",
          "orig-publish-date": "2025-03-05",
          "originChamber": "SENATE",
          "update-date": "2025-07-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s866v00",
            "update-date": "2025-07-14"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Accelerating Broadband Permits Act</strong></p><p>This bill makes specified changes to processes for federal review of certain communications and broadband infrastructure projects.\u00a0</p><p>Specifically, the bill requires executive branch agencies to identify and address factors that contribute to delays in their review of applications for easements, rights-of-way, or leases related to communications infrastructure projects. (Under current law, executive branch agencies with control over buildings or property may grant such easements, rights-of-way, or leases to entities seeking to install, construct, modify, or maintain communications facilities. Generally, agencies must act on such applications within 270 days.)\u00a0</p><p>Under the bill, agencies must develop controls to ensure accurate tracking of processing times for such applications and take action to address factors contributing to delays as they occur. Agencies must also establish methods to alert employees when the agency is at risk of failing to meet the 270-day deadline with respect to a particular application. (These provisions were recommended by the Government Accountability Office in an April 2024 report to Congress entitled <em>Broadband Deployment: Agencies Should Take Steps to Better Meet Deadline for Processing Permits</em>.)\u00a0</p><p>Separately, the bill lowers the cost threshold for certain broadband infrastructure projects to qualify as <em>covered projects</em> under the Fixing America's Surface Transportation (FAST) Act from $200 million to $5 million. Such projects qualify for expedited federal environmental review.</p>"
        },
        "title": "Accelerating Broadband Permits Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s866.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating Broadband Permits Act</strong></p><p>This bill makes specified changes to processes for federal review of certain communications and broadband infrastructure projects.\u00a0</p><p>Specifically, the bill requires executive branch agencies to identify and address factors that contribute to delays in their review of applications for easements, rights-of-way, or leases related to communications infrastructure projects. (Under current law, executive branch agencies with control over buildings or property may grant such easements, rights-of-way, or leases to entities seeking to install, construct, modify, or maintain communications facilities. Generally, agencies must act on such applications within 270 days.)\u00a0</p><p>Under the bill, agencies must develop controls to ensure accurate tracking of processing times for such applications and take action to address factors contributing to delays as they occur. Agencies must also establish methods to alert employees when the agency is at risk of failing to meet the 270-day deadline with respect to a particular application. (These provisions were recommended by the Government Accountability Office in an April 2024 report to Congress entitled <em>Broadband Deployment: Agencies Should Take Steps to Better Meet Deadline for Processing Permits</em>.)\u00a0</p><p>Separately, the bill lowers the cost threshold for certain broadband infrastructure projects to qualify as <em>covered projects</em> under the Fixing America's Surface Transportation (FAST) Act from $200 million to $5 million. Such projects qualify for expedited federal environmental review.</p>",
      "updateDate": "2025-07-14",
      "versionCode": "id119s866"
    },
    "title": "Accelerating Broadband Permits Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating Broadband Permits Act</strong></p><p>This bill makes specified changes to processes for federal review of certain communications and broadband infrastructure projects.\u00a0</p><p>Specifically, the bill requires executive branch agencies to identify and address factors that contribute to delays in their review of applications for easements, rights-of-way, or leases related to communications infrastructure projects. (Under current law, executive branch agencies with control over buildings or property may grant such easements, rights-of-way, or leases to entities seeking to install, construct, modify, or maintain communications facilities. Generally, agencies must act on such applications within 270 days.)\u00a0</p><p>Under the bill, agencies must develop controls to ensure accurate tracking of processing times for such applications and take action to address factors contributing to delays as they occur. Agencies must also establish methods to alert employees when the agency is at risk of failing to meet the 270-day deadline with respect to a particular application. (These provisions were recommended by the Government Accountability Office in an April 2024 report to Congress entitled <em>Broadband Deployment: Agencies Should Take Steps to Better Meet Deadline for Processing Permits</em>.)\u00a0</p><p>Separately, the bill lowers the cost threshold for certain broadband infrastructure projects to qualify as <em>covered projects</em> under the Fixing America's Surface Transportation (FAST) Act from $200 million to $5 million. Such projects qualify for expedited federal environmental review.</p>",
      "updateDate": "2025-07-14",
      "versionCode": "id119s866"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s866is.xml"
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
      "title": "Accelerating Broadband Permits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accelerating Broadband Permits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require executive agencies to take steps to better meet the statutory deadline for processing communications use applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:42Z"
    }
  ]
}
```
