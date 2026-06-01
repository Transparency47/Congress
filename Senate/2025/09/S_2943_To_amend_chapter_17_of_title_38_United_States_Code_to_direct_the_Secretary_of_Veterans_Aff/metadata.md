# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2943?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2943
- Title: ACE Veterans Act
- Congress: 119
- Bill type: S
- Bill number: 2943
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2025-12-05T22:56:30Z
- Update date including text: 2025-12-05T22:56:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2943",
    "number": "2943",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "ACE Veterans Act",
    "type": "S",
    "updateDate": "2025-12-05T22:56:30Z",
    "updateDateIncludingText": "2025-12-05T22:56:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T18:28:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "HI"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "WA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2943is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2943\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Ms. Duckworth (for herself, Ms. Hirono , Mr. Fetterman , Mrs. Murray , Ms. Alsobrooks , Mr. Heinrich , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend chapter 17 of title 38, United States Code, to direct the Secretary of Veterans Affairs to allow a veteran to receive a full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Contraception Expansion for Veterans Act or the ACE Veterans Act .\n#### 2. Full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products\n##### (a) Full year supply\nSubchapter II of chapter 17 of title 38, United States Code, is amended by inserting after section 1720L the following new section:\n1720M. Full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products (a) Availability of full-Year supply The Secretary shall ensure that a veteran who is enrolled in the system of annual patient enrollment under section 1705 of this title and to whom a medical provider of the Department prescribes contraceptive pills, transdermal patches, vaginal rings, or other contraceptive products may elect to fill such prescription as a full-year supply. (b) Notice A medical provider of the Department who prescribes to a veteran contraceptive pills, transdermal patches, vaginal rings, or other contraceptive products shall notify the veteran of the option to fill the prescription as a full-year supply. (c) Contraceptive product defined In this section, the term contraceptive product means any drug, device, or biological product intended for use in the prevention of pregnancy, whether specifically intended to prevent pregnancy or for other health needs, that is approved, cleared, authorized, or licensed under section 505, 510(k), 513(f)(2), 515, or 564 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 , 360(k), 360c(f)(2), 360e, 360bbb\u20133) or section 351 of the Public Health Service Act ( 42 U.S.C. 262 ). .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1720L the following new item:\n1720M. Full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products. .",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-09-30",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "5665",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ACE Veterans Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-17T16:31:58Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2943is.xml"
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
      "title": "ACE Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACE Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Contraception Expansion for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 17 of title 38, United States Code, to direct the Secretary of Veterans Affairs to allow a veteran to receive a full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:15Z"
    }
  ]
}
```
