# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/112
- Title: Proposing an amendment to the Constitution of the United States related to the public debt.
- Congress: 119
- Bill type: HJRES
- Bill number: 112
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2025-09-05T16:12:26Z
- Update date including text: 2025-09-05T16:12:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/112",
    "number": "112",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States related to the public debt.",
    "type": "HJRES",
    "updateDate": "2025-09-05T16:12:26Z",
    "updateDateIncludingText": "2025-09-05T16:12:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
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
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:03:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres112ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 112\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Burlison submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States related to the public debt.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. Total outlays of the Government of the United States shall not exceed total receipts of the Government of the United States at any point in time unless the excess of outlays over receipts is financed exclusively by debt issued in strict conformity with this article. 2. Outstanding debt shall not exceed authorized debt, which initially shall be an amount equal to 105 percent of the outstanding debt on the effective date of this article. Authorized debt shall not be increased above its aforesaid initial amount unless such increase is first approved by the legislatures of the several States as provided in section 3. 3. From time to time, Congress may increase authorized debt to an amount in excess of its initial amount set by section 2 only if it first publicly refers to the legislatures of the several States an unconditional, single subject measure proposing the amount of such increase, in such form as provided by law, and the measure is thereafter publicly and unconditionally approved by a simple majority of the legislatures of the several States, in such form as provided respectively by State law: Provided, That no inducement requiring an expenditure or tax levy shall be demanded, offered or accepted as a quid pro quo for such approval. If such approval is not obtained within sixty (60) calendar days after referral then the measure shall be deemed disapproved and the authorized debt shall thereby remain unchanged. 4. Whenever the outstanding debt exceeds 98 percent of the debt limit set by section 2, the President shall enforce said limit by publicly designating specific expenditures for impoundment in an amount sufficient to ensure outstanding debt shall not exceed the authorized debt. Said impoundment shall become effective thirty (30) days thereafter, unless Congress first designates an alternate impoundment of the same or greater amount by concurrent resolution, which shall become immediately effective. The failure of the President to designate or enforce the required impoundment is an impeachable misdemeanor. Any purported issuance or incurrence of any debt in excess of the debt limit set by section 2 is void. 5. No bill that provides for a new or increased general revenue tax shall become law unless approved by a two-thirds roll call vote of the whole number of each House of Congress. However, this requirement shall not apply to any bill that provides for a new end user sales tax which would completely replace every existing income tax levied by the Government of the United States; or for the reduction or elimination of an exemption, deduction, or credit allowed under an existing general revenue tax. 6. For purposes of this article, debt means any obligation backed by the full faith and credit of the Government of the United States; outstanding debt means all debt held in any account and by any entity at a given point in time; authorized debt means the maximum total amount of debt that may be lawfully issued and outstanding at any single point in time under this article; total outlays of the Government of the United States means all expenditures of the Government of the United States from any source; total receipts of the Government of the United States means all tax receipts and other income of the Government of the United States, excluding proceeds from its issuance or incurrence of debt or any type of liability; impoundment means a proposal not to spend all or part of a sum of money appropriated by Congress; and general revenue tax means any income tax, sales tax, or value-added tax levied by the Government of the United States excluding imposts and duties. 7. This article is immediately operative upon ratification, self-enforcing, and Congress may enact conforming legislation to facilitate enforcement. .",
      "versionDate": "2025-08-15",
      "versionType": "IH"
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-09-05T16:12:26Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres112ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Proposing an amendment to the Constitution of the United States related to the public debt.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-26T14:03:18Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States related to the public debt.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-16T08:05:47Z"
    }
  ]
}
```
