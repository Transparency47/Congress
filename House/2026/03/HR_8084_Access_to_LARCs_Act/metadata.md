# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8084?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8084
- Title: Access to LARCs Act
- Congress: 119
- Bill type: HR
- Bill number: 8084
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-14T13:24:48Z
- Update date including text: 2026-04-14T13:24:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8084",
    "number": "8084",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Access to LARCs Act",
    "type": "HR",
    "updateDate": "2026-04-14T13:24:48Z",
    "updateDateIncludingText": "2026-04-14T13:24:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T14:01:40Z",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "IA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8084ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8084\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Mrs. Hinson (for herself, Mrs. Miller-Meeks , Ms. Malliotakis , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to conduct a study and submit to Congress a report on contraceptive access at community health centers in health care deserts.\n#### 1. Short title\nThis Act may be cited as the Access to LARCs Act .\n#### 2. Study and report on access to range of contraceptive methods at community health centers\n##### (a) Study\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall conduct a study on the access of women in need to a range of contraceptive methods at community health centers located in health care deserts. Such study shall\u2014\n**(1)**\ninclude analysis related to reimbursement, inventory stocking, provider training, patient education, and other barriers to community health centers providing a range of contraceptive methods; and\n**(2)**\nindicate which community health centers are recipients of funding under title X of the Public Health Service Act ( 42 U.S.C. 300 et seq. ).\n##### (b) Report\nNot later than 180 days after the date of enactment of this Act, the Secretary shall submit to Congress a report describing the results of the study under subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Community health center**\nThe term community health center means a health center (as defined in section 330(a) of the Public Health Service Act ( 42 U.S.C. 254b(a) )).\n**(2) Contraceptive method**\nThe term contraceptive method means\u2014\n**(A)**\na drug or device (as such terms are defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )), or combination product, approved for use under the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 et seq. ) as a method of contraception, except when such drug, device, or combination product is used on- or off-label as an emergency contraceptive;\n**(B)**\nsexual risk avoidance education; and\n**(C)**\nnatural family planning or other fertility-based methods of family planning.\n**(3) Health care desert**\nThe term health care desert means a State or political subdivision thereof with less than 1 community health center for every 1,000 women in need.\n**(4) Range of contraceptive methods**\nThe term range of contraceptive methods means 2 or more contraceptive methods.\n**(5) Women in need**\nThe term women in need means women eligible for benefits under a Federal health care program (as defined in section 1128B(f) of the Social Security Act (42 U.S.C. 1320a\u20137b(f))).",
      "versionDate": "2026-03-25",
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
        "name": "Health",
        "updateDate": "2026-04-14T13:24:48Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8084ih.xml"
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
      "title": "Access to LARCs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to LARCs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to conduct a study and submit to Congress a report on contraceptive access at community health centers in health care deserts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T03:48:31Z"
    }
  ]
}
```
