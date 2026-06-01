# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2918?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2918
- Title: Family Business Legacy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2918
- Origin chamber: House
- Introduced date: 2025-04-14
- Update date: 2025-05-12T20:04:05Z
- Update date including text: 2025-05-12T20:04:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-14: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-14: Introduced in House

## Actions

- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-14",
    "latestAction": {
      "actionDate": "2025-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2918",
    "number": "2918",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
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
    "title": "Family Business Legacy Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-12T20:04:05Z",
    "updateDateIncludingText": "2025-05-12T20:04:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-14",
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
      "actionDate": "2025-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-14",
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
          "date": "2025-04-14T13:01:20Z",
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
      "sponsorshipDate": "2025-04-14",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2918ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2918\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2025 Mr. Steube (for himself and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from the value of taxable estates bequests to certain exempt organizations.\n#### 1. Short title\nThis Act may be cited as the Family Business Legacy Act of 2025 .\n#### 2. Exclusion of bequests to certain exempt organizations from value of taxable estate\n##### (a) In general\nPart IV of subchapter A of chapter 11 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n2059. Bequests to certain exempt organizations (a) In general For purposes of the tax imposed by section 2001, the value of the taxable estate shall be determined by deducting from the value of the gross estate the amount of all bequests, devises, or transfers to or for the use of any organization exempt from tax under section 501(a) and described in paragraph (4), (5), or (6) of section 501(c). (b) Powers of appointment Property includible in the decedent's gross estate under section 2041 (relating to powers of appointment) received by a donee described in this section shall, for purposes of this section, be considered a bequest of such decedent. (c) Death taxes payable out of bequests If the tax imposed by section 2001, or any estate, succession, legacy, or inheritance taxes, are, either by the terms of the will, by the law of the jurisdiction under which the estate is administered, or by the law of the jurisdiction imposing the particular tax, payable in whole or in part out of the bequests, legacies, or devises otherwise deductible under this section, then the amount deductible under this section shall be the amount of such bequests, legacies, or devises reduced by the amount of such taxes. (d) Limitation on deduction The amount of the deduction under this section for any transfer shall not exceed the value of the transferred property required to be included in the gross estate. (e) Disallowance of deductions in certain cases Where an interest in property (other than an interest described in section 170(f)(3)(B)) passes or has passed from the decedent to a person, or for a use, described in subsection (a), and an interest (other than an interest which is extinguished upon the decedent's death) in the same property passes or has passed (for less than an adequate and full consideration in money or money's worth) from the decedent to a person, or for a use, not described in subsection (a), no deduction shall be allowed under this section for the interest which passes or has passed to the person, or for the use, described in subsection (a) unless such interest, whether in the form of a remainder interest, lead interest, or any other interest, is in the form of qualified interest (within the meaning of section 2702(b)) and valued under the rules of section 7520. .\n##### (b) Conforming amendment\nThe table of sections for part IV of subchapter A of chapter 11 is amended by inserting at the end the following new item:\nSec. 2059. Bequests to certain exempt organizations. .\n##### (c) Effective date\nThe amendments made by the section shall apply to estates of decedents dying or bequests, devises, or transfers made after December 31, 2025.",
      "versionDate": "2025-04-14",
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
        "updateDate": "2025-05-12T20:04:05Z"
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
      "date": "2025-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2918ih.xml"
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
      "title": "Family Business Legacy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Family Business Legacy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude from the value of taxable estates bequests to certain exempt organizations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T03:18:27Z"
    }
  ]
}
```
