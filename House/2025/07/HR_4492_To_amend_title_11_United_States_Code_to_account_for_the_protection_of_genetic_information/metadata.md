# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4492
- Title: Don’t Sell My DNA Act
- Congress: 119
- Bill type: HR
- Bill number: 4492
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-12-05T22:54:31Z
- Update date including text: 2025-12-05T22:54:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4492",
    "number": "4492",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Don\u2019t Sell My DNA Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:54:31Z",
    "updateDateIncludingText": "2025-12-05T22:54:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NC"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4492ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4492\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Cline (for himself and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 11, United States Code, to account for the protection of genetic information in bankruptcy.\n#### 1. Short title\nThis Act may be cited as the Don\u2019t Sell My DNA Act .\n#### 2. Amendments to title 11, United States Code, relating to protection of genetic information\n##### (a) In general\nTitle 11, United States Code, is amended\u2014\n**(1)**\nin section 101(41A)(A)\u2014\n**(A)**\nin clause (v), by striking or at the end; and\n**(B)**\nby adding at the end the following:\n(vii) genetic information, as defined in section 201 of the Genetic Information Nondiscrimination Act of 2008 ( 42 U.S.C. 2000ff ); or ;\n**(2)**\nin section 363\u2014\n**(A)**\nin subsection (b)(1)(B), by striking clause (ii) and inserting the following:\n(ii) finding that no showing was made that such sale or such lease would violate applicable nonbankruptcy law, provided, however, that no use, sale, or lease shall be approved if the personally identifiable information consists, in whole or in part, of genetic information (as defined in section 201 of the Genetic Information Nondiscrimination Act of 2008 ( 42 U.S.C. 2000ff )), unless all affected persons, including non-parties, have affirmatively consented in writing to such use, sale, or lease after the commencement of the case. ; and\n**(B)**\nby adding at the end the following:\n(q) Any use, sale, or lease of genetic information (as defined in section 201 of the Genetic Information Nondiscrimination Act of 2008 ( 42 U.S.C. 2000ff )) shall not be considered final and valid unless each person whose genetic information would be subject to such use, sale, or lease is provided with actual prior written notice of such use, sale, or lease. ; and\n**(3)**\nin section 1107, by adding at the end the following:\n(c) A trustee serving in a case under this chapter or debtor in possession shall delete, using methods proscribed by the court (which may include the Guidelines for Media Sanitization issued by the National Institute of Standards and Technology (NIST Special Publication 800\u201388), or any successor thereto), any genetic information (as defined in section 201 of the Genetic Information Nondiscrimination Act of 2008 ( 42 U.S.C. 2000ff )) that was property of the estate and that was not subject to a sale, lease, or other disposition under section 363 of this title. .\n##### (b) Effective date\nThe amendments made by this section\u2014\n**(1)**\nshall take effect on the date of enactment of this Act; and\n**(2)**\nshall apply to any case under title 11, United States Code, that is\u2014\n**(A)**\npending as of the date of enactment of this Act; or\n**(B)**\ncommenced or reopened on or after the date of enactment of this Act.",
      "versionDate": "2025-07-17",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1916",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Don\u2019t Sell My DNA Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-11T15:42:19Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4492ih.xml"
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
      "title": "Don\u2019t Sell My DNA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don\u2019t Sell My DNA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 11, United States Code, to account for the protection of genetic information in bankruptcy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:35Z"
    }
  ]
}
```
