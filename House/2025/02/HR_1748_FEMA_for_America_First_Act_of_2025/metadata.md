# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1748?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1748
- Title: FEMA for America First Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1748
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-12-17T16:32:17Z
- Update date including text: 2025-12-17T16:32:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-27 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-27 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1748",
    "number": "1748",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "FEMA for America First Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-17T16:32:17Z",
    "updateDateIncludingText": "2025-12-17T16:32:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:11:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-27T23:03:27Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1748ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1748\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Steube (for himself, Mr. Weber of Texas , and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide that aliens who are not qualified aliens are ineligible for certain assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FEMA for America First Act of 2025 .\n#### 2. Eligibility of aliens for assistance\nTitle IV of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 et seq. ) is amended by adding at the end the following:\n431. Eligibility of aliens for assistance (a) In general With respect to an alien otherwise eligible for any assistance provided to individuals under this Act, only a qualified alien shall be eligible for such assistance. (b) Definitions In this section: (1) In general Except as otherwise provided, the terms used have the same meaning given such terms in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ). (2) Qualified alien The term qualified alien has the meaning given such term in section 431 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1641 ), except that such term does not include\u2014 (A) an alien who\u2014 (i) is granted asylum under section 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ); and (ii) has not sought adjustment to the status of alien lawfully admitted for permanent residence under section 209(b) of such Act; (B) a refugee who\u2014 (i) is admitted to the United States under section 207 of such Act; and (ii) has not sought adjustment to the status of alien lawfully admitted for permanent residence under section 209(a) of such Act; or (C) an alien who is paroled into the United States under section 212(d)(5) of such Act. .",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-16T17:15:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
    "originChamber": "House",
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
          "measure-id": "id119hr1748",
          "measure-number": "1748",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-12-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1748v00",
            "update-date": "2025-12-17"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>FEMA for America First Act of 2025</strong></p><p>This bill restricts the eligibility of non-U.S. nationals (<em>aliens</em> under federal law) for federal disaster assistance benefits by eliminating eligibility for individuals with certain immigration statuses.\u00a0</p><p>Under current law, a\u00a0non-U.S. national must have one of several specific immigration statuses (e.g., lawful permanent resident, parolee, or refugee) to be eligible for federal disaster assistance provided to individuals (e.g., the Federal Emergency Management Agency's (FEMA's) Individuals and Households Program or disaster unemployment assistance).</p><p>The bill narrows the immigration statuses eligible for disaster assistance to individuals by making\u00a0non-U.S. nationals ineligible for such assistance if they are</p><ul><li>a parolee (i.e., paroled into the United States temporarily for urgent humanitarian reasons or significant public benefit),\u00a0</li><li>an asylee that has not sought adjustment to lawful permanent resident status, or\u00a0</li><li>a refugee that has not sought adjustment to lawful permanent resident status.</li></ul>"
        },
        "title": "FEMA for America First Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1748.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA for America First Act of 2025</strong></p><p>This bill restricts the eligibility of non-U.S. nationals (<em>aliens</em> under federal law) for federal disaster assistance benefits by eliminating eligibility for individuals with certain immigration statuses.\u00a0</p><p>Under current law, a\u00a0non-U.S. national must have one of several specific immigration statuses (e.g., lawful permanent resident, parolee, or refugee) to be eligible for federal disaster assistance provided to individuals (e.g., the Federal Emergency Management Agency's (FEMA's) Individuals and Households Program or disaster unemployment assistance).</p><p>The bill narrows the immigration statuses eligible for disaster assistance to individuals by making\u00a0non-U.S. nationals ineligible for such assistance if they are</p><ul><li>a parolee (i.e., paroled into the United States temporarily for urgent humanitarian reasons or significant public benefit),\u00a0</li><li>an asylee that has not sought adjustment to lawful permanent resident status, or\u00a0</li><li>a refugee that has not sought adjustment to lawful permanent resident status.</li></ul>",
      "updateDate": "2025-12-17",
      "versionCode": "id119hr1748"
    },
    "title": "FEMA for America First Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA for America First Act of 2025</strong></p><p>This bill restricts the eligibility of non-U.S. nationals (<em>aliens</em> under federal law) for federal disaster assistance benefits by eliminating eligibility for individuals with certain immigration statuses.\u00a0</p><p>Under current law, a\u00a0non-U.S. national must have one of several specific immigration statuses (e.g., lawful permanent resident, parolee, or refugee) to be eligible for federal disaster assistance provided to individuals (e.g., the Federal Emergency Management Agency's (FEMA's) Individuals and Households Program or disaster unemployment assistance).</p><p>The bill narrows the immigration statuses eligible for disaster assistance to individuals by making\u00a0non-U.S. nationals ineligible for such assistance if they are</p><ul><li>a parolee (i.e., paroled into the United States temporarily for urgent humanitarian reasons or significant public benefit),\u00a0</li><li>an asylee that has not sought adjustment to lawful permanent resident status, or\u00a0</li><li>a refugee that has not sought adjustment to lawful permanent resident status.</li></ul>",
      "updateDate": "2025-12-17",
      "versionCode": "id119hr1748"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1748ih.xml"
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
      "title": "FEMA for America First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FEMA for America First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide that aliens who are not qualified aliens are ineligible for certain assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:37Z"
    }
  ]
}
```
