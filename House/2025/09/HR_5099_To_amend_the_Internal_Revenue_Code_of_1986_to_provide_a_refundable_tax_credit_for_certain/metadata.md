# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5099?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5099
- Title: SAFES Act
- Congress: 119
- Bill type: HR
- Bill number: 5099
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2025-09-05T16:07:42Z
- Update date including text: 2025-09-05T16:07:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5099",
    "number": "5099",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "SAFES Act",
    "type": "HR",
    "updateDate": "2025-09-05T16:07:42Z",
    "updateDateIncludingText": "2025-09-05T16:07:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:02:50Z",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "RI"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5099ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5099\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Ms. Williams of Georgia (for herself, Mr. Amo , and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a refundable tax credit for certain gun safes.\n#### 1. Short title\nThis Act may be cited as the Storing All Firearms Effectively and Safely Act or as the SAFES Act .\n#### 2. Refundable credit for certain gun safes\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n36C. Credit for certain gun safes (a) In general In the case of an individual, there shall be allowed as a credit against the tax imposed by this subtitle for any taxable year an amount equal to 90 percent of the aggregate amount paid or incurred by the taxpayer during the taxable year for\u2014 (1) in the case of any taxable year beginning before January 1, 2031, any gun safe, and (2) in the case of any taxable year beginning after December 31, 2030, any gun safe which is of a type which has been determined by the Secretary of Health and Human Services in the report made publicly available under section 3 of the SAFES Act to be highly effective in preventing unauthorized access. (b) Limitation The amount allowed as a credit under subsection (a) with respect to any taxpayer for any taxable year shall not exceed the excess (if any) of\u2014 (1) $500 ($1,000 in the case of a joint return), over (2) the aggregate amount of credits allowed under this section with respect to such taxpayer during the 6 preceding taxable years. (c) Gun safe For purposes of this section\u2014 (1) In general The term gun safe means\u2014 (A) any device that is designed and marketed for the principal purpose of denying unauthorized access to a firearm or ammunition, and (B) any safe, gun safe, gun case, lock box, or other device that is secured by a combination lock, key lock, or lock based on biometric information which, once locked, is incapable of being opened without the combination, key, or biometric information, respectively. (2) Exclusion of used safes Such term shall not include any property unless the original use of such property begins with the taxpayer. (d) Prohibition on collection of information regarding firearms No taxpayer shall be required, as a condition of the credit allowed under this section, to provide any information with respect to any firearms owned by the taxpayer. .\n##### (b) Conforming amendments\n**(1)**\nSection 6211(b)(4)(A) of the Internal Revenue Code of 1986 is amended by inserting 36C, after 36B, .\n**(2)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n**(3)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Credit for certain gun safes. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Report on most effective gun safes\nNot later than the date which is 5 years after the date of the enactment of this Act, the Secretary of Health and Human Services shall make publicly available a report indicating which types of gun safes (as defined section 36C(c) of the Internal Revenue Code of 1986) are highly effective in preventing unauthorized access.",
      "versionDate": "2025-09-02",
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
        "name": "Taxation",
        "updateDate": "2025-09-05T16:07:42Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5099ih.xml"
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
      "title": "SAFES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-05T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Storing All Firearms Effectively and Safely Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-05T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a refundable tax credit for certain gun safes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-05T04:18:21Z"
    }
  ]
}
```
