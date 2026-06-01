# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3324
- Title: Safer Shrimp Imports Act
- Congress: 119
- Bill type: HR
- Bill number: 3324
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2026-05-22T08:08:45Z
- Update date including text: 2026-05-22T08:08:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3324",
    "number": "3324",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Safer Shrimp Imports Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:45Z",
    "updateDateIncludingText": "2026-05-22T08:08:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "LA"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "LA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3324ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3324\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Ezell (for himself, Mr. Carter of Louisiana , and Ms. Letlow ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to provide for the inspection of foreign facilities that manufacture, process, pack, or hold shrimp for consumption in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safer Shrimp Imports Act .\n#### 2. Shrimp manufactured, processed, packed, or held at overseas facilities\n##### (a) In general\nSection 807 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 384c ) is amended by adding at the end the following:\n(c) Requirements for foreign shrimp facilities (1) In general Notwithstanding any other provision of law, not later than 180 days after the date of enactment of this subsection, the Secretary shall seek to enter into arrangements and agreements under subsection (a)(1) with the foreign government of each foreign country with 1 or more foreign facilities registered under section 415 that manufacture, process, pack, or hold shrimp for consumption in the United States. (2) Requirements for shrimp Beginning on the date that is 1 year after the date of enactment of this subsection, shrimp shall be refused admission into the United States if it is manufactured, processed, packed, or held in a foreign country\u2014 (A) the government of which does not enter into an arrangement or agreement with the Secretary under paragraph (1); or (B) the food inspection system of which does not meet the criteria described in paragraph (3). (3) Criteria The criteria described in this paragraph with respect to a food inspection system is that the food inspection system (as demonstrated to the Secretary by the applicable foreign government) is equivalent to the food inspection system of the Food and Drug Administration with respect to shrimp, including by providing\u2014 (A) staffing that ensures uniform enforcement of applicable laws and regulations; and (B) enforcement of laws and regulations that address the conditions under which shrimp is raised and transported to processing establishments. (4) Demonstration A foreign government seeking to demonstrate that its food inspection system meets the criteria described in paragraph (3) shall provide to the Secretary copies of all laws, regulations, and other information pertaining to such food inspection system. .\n##### (b) Adulteration\nSection 402 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 342 ) is amended by adding at the end the following:\n(j) If it is shrimp imported or offered for import into the United States and the shrimp has been manufactured, processed, packed, or held in a foreign country the government or food inspection system of which does not comply with the applicable requirements of section 807(c). .\n##### (c) Report to congress\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary of Health and Human Services shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that describes the implementation of the amendments made by subsections (a) and (b).",
      "versionDate": "2025-05-13",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "667",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safer Shrimp Imports Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-05T14:19:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-13",
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
          "measure-id": "id119hr3324",
          "measure-number": "3324",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-13",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3324v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-05-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safer Shrimp Imports Act</strong></p><p>This bill prohibits the importation of shrimp from countries that do not have food inspection systems equivalent to the Food and Drug Administration (FDA) inspection system for shrimp, or that have not entered into an agreement with the FDA facilitating U.S. inspection of their food facilities. \u00a0</p><p>Specifically, the FDA must seek to enter into arrangements and agreements with the government of each country with at least one facility that manufactures, processes, packs, or holds shrimp for consumption in the United States to facilitate FDA inspection of such facilities.\u00a0</p><p>The bill prohibits the importation of shrimp that is manufactured, processed, packed, or held in a country (1) that has not entered into an inspection arrangement or agreement with the FDA, or (2) the food inspection system of which is not equivalent to the FDA\u2019s food inspection system with respect to shrimp. To be considered equivalent, a country\u2019s food inspection system must include staffing that ensures uniform enforcement of applicable laws and regulations, and must provide for the enforcement of laws and regulations that address conditions under which shrimp are raised and transported to processing facilities. \u00a0</p><p>Further, shrimp imported or offered for import into the United States that have been manufactured, processed, packed, or held in a country that is not compliant with these requirements are deemed adulterated, and thus may not be introduced into interstate commerce.\u00a0</p>"
        },
        "title": "Safer Shrimp Imports Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3324.xml",
    "summary": {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safer Shrimp Imports Act</strong></p><p>This bill prohibits the importation of shrimp from countries that do not have food inspection systems equivalent to the Food and Drug Administration (FDA) inspection system for shrimp, or that have not entered into an agreement with the FDA facilitating U.S. inspection of their food facilities. \u00a0</p><p>Specifically, the FDA must seek to enter into arrangements and agreements with the government of each country with at least one facility that manufactures, processes, packs, or holds shrimp for consumption in the United States to facilitate FDA inspection of such facilities.\u00a0</p><p>The bill prohibits the importation of shrimp that is manufactured, processed, packed, or held in a country (1) that has not entered into an inspection arrangement or agreement with the FDA, or (2) the food inspection system of which is not equivalent to the FDA\u2019s food inspection system with respect to shrimp. To be considered equivalent, a country\u2019s food inspection system must include staffing that ensures uniform enforcement of applicable laws and regulations, and must provide for the enforcement of laws and regulations that address conditions under which shrimp are raised and transported to processing facilities. \u00a0</p><p>Further, shrimp imported or offered for import into the United States that have been manufactured, processed, packed, or held in a country that is not compliant with these requirements are deemed adulterated, and thus may not be introduced into interstate commerce.\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr3324"
    },
    "title": "Safer Shrimp Imports Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safer Shrimp Imports Act</strong></p><p>This bill prohibits the importation of shrimp from countries that do not have food inspection systems equivalent to the Food and Drug Administration (FDA) inspection system for shrimp, or that have not entered into an agreement with the FDA facilitating U.S. inspection of their food facilities. \u00a0</p><p>Specifically, the FDA must seek to enter into arrangements and agreements with the government of each country with at least one facility that manufactures, processes, packs, or holds shrimp for consumption in the United States to facilitate FDA inspection of such facilities.\u00a0</p><p>The bill prohibits the importation of shrimp that is manufactured, processed, packed, or held in a country (1) that has not entered into an inspection arrangement or agreement with the FDA, or (2) the food inspection system of which is not equivalent to the FDA\u2019s food inspection system with respect to shrimp. To be considered equivalent, a country\u2019s food inspection system must include staffing that ensures uniform enforcement of applicable laws and regulations, and must provide for the enforcement of laws and regulations that address conditions under which shrimp are raised and transported to processing facilities. \u00a0</p><p>Further, shrimp imported or offered for import into the United States that have been manufactured, processed, packed, or held in a country that is not compliant with these requirements are deemed adulterated, and thus may not be introduced into interstate commerce.\u00a0</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr3324"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3324ih.xml"
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
      "title": "Safer Shrimp Imports Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safer Shrimp Imports Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to provide for the inspection of foreign facilities that manufacture, process, pack, or hold shrimp for consumption in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T05:48:39Z"
    }
  ]
}
```
