# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5665
- Title: ACE Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 5665
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-01-09T09:06:56Z
- Update date including text: 2026-01-09T09:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-03 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-03 - Committee: Referred to the Subcommittee on Health.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5665",
    "number": "5665",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "ACE Veterans Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:56Z",
    "updateDateIncludingText": "2026-01-09T09:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-03T14:02:15Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5665ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5665\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Ms. Underwood introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend chapter 17 of title 38, United States Code, to direct the Secretary of Veterans Affairs to allow a veteran to receive a full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Contraception Expansion for Veterans Act or the ACE Veterans Act .\n#### 2. Full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products\n##### (a) Full-Year supply\nSubchapter II of chapter 17 of title 38, United States Code, is amended by inserting after section 1720L the following new section:\n1720M. Full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products (a) Availability of full-Year supply The Secretary shall ensure that a veteran who is enrolled in the system of annual patient enrollment under section 1705 of this title and to whom a medical provider of the Department prescribes contraceptive pills, transdermal patches, vaginal rings, or other contraceptive products may elect to fill such prescription as a full-year supply. (b) Notice A medical provider of the Department who prescribes to a veteran contraceptive pills, transdermal patches, vaginal rings, or other contraceptive products shall notify the veteran of the option to fill the prescription as a full-year supply. (c) Contraceptive product defined In this section, the term contraceptive product means any drug, device, or biological product intended for use in the prevention of pregnancy, whether specifically intended to prevent pregnancy or for other health needs, that is approved, cleared, authorized, or licensed under section 505, 510(k), 513(f)(2), 515, or 564 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 , 360(k), 360c(f)(2), 360e, 360bbb\u20133) or section 351 of the Public Health Service Act ( 42 U.S.C. 262 ). .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1720L the following new item:\n1720M. Full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products. .",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-09-30",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "2943",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ACE Veterans Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:38:20Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5665ih.xml"
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
      "title": "ACE Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T02:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACE Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T02:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to Contraception Expansion for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T02:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 17 of title 38, United States Code, to direct the Secretary of Veterans Affairs to allow a veteran to receive a full-year supply of contraceptive pills, transdermal patches, vaginal rings, and other contraceptive products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T02:33:21Z"
    }
  ]
}
```
