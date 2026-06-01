# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3247
- Title: SAFE Home Act
- Congress: 119
- Bill type: HR
- Bill number: 3247
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-12-05T22:47:49Z
- Update date including text: 2025-12-05T22:47:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3247",
    "number": "3247",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "SAFE Home Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:47:49Z",
    "updateDateIncludingText": "2025-12-05T22:47:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "GA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "GA"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3247ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3247\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mrs. Miller of Illinois (for herself and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo prohibit entities receiving Federal assistance that are involved in adoption or foster care placements from delaying or denying placements under certain conditions.\n#### 1. Short title\nThis Act may be cited as the Sensible Adoption For Every Home Act or the SAFE Home Act .\n#### 2. State plan requirement under the Federal foster care and adoption assistance program\n##### (a) In general\nSection 471(a) of the Social Security Act ( 42 U.S.C. 671(a) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (36);\n**(2)**\nby striking the period at the end of paragraph (37) and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(38) (A) prohibits any entity that receives Federal assistance and is involved in adoption or foster care placements from delaying or denying the placement of a minor child for adoption or into foster care, or otherwise discriminating in making a placement decision with a prospective or actual adoptive or foster parent, for any of the following reasons: (i) The parent raises, cares for, and addresses a child in a manner consistent with the child\u2019s sex. (ii) The parent declines to consent to a child receiving any medical, surgical, pharmacological, or psychological treatment or other medical or mental health service for the purpose of attempting to alter the appearance of, or to validate a child\u2019s perception of, the child\u2019s sex, if the appearance or perception is inconsistent with the child\u2019s sex. (iii) The parent declines to consent to an amendment or alteration to a child\u2019s birth certificate, passport, driver\u2019s license, school records, or other government-issued identification document, if the amendment or alteration is inconsistent with the child\u2019s sex; and (B) for purposes of this paragraph, defines\u2014 (i) the term sex as biological sex, either male or female; (ii) the term female as an individual who has, had, will have, or but for a developmental or genetic anomaly or historical accident would have, a reproductive system that at some point produces, transports, and utilizes eggs for fertilization; and (iii) the term male as an individual who has, had, will have, or but for a developmental or genetic anomaly or historical accident would have, a reproductive system that at some point produces, transports, and utilizes sperm for fertilization. .\n##### (b) Effective date\n**(1) In general**\nThe amendment made by this Act shall take effect on the 1st day of the 1st fiscal quarter beginning on or after the date of the enactment of this Act, and shall apply to payments under part E of title IV of the Social Security Act for calendar quarters beginning on or after such date.\n**(2) Delay permitted if state legislation required**\nIf the Secretary of Health and Human Services determines that State legislation (other than legislation appropriating funds) is required in order for a State plan developed pursuant to part E of title IV of the Social Security Act to meet the additional requirements imposed by the amendments made by this Act, the plan shall not be regarded as failing to meet any of the additional requirements before the 1st day of the 1st calendar quarter beginning after the first regular session of the State legislature that begins after the date of the enactment of this Act. For purposes of the preceding sentence, if the State has a 2-year legislative session, each year of the session is deemed to be a separate regular session of the State legislature.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1658",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAFE Home Act",
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
        "name": "Families",
        "updateDate": "2025-05-21T13:50:32Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3247ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit entities receiving Federal assistance that are involved in adoption or foster care placements from delaying or denying placements under certain conditions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:32Z"
    },
    {
      "title": "SAFE Home Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sensible Adoption For Every Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:25Z"
    }
  ]
}
```
