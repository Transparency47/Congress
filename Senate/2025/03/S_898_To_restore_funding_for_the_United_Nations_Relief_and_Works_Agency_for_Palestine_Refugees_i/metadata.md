# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/898?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/898
- Title: UNRWA Funding Emergency Restoration Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 898
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-12-05T22:08:28Z
- Update date including text: 2025-12-05T22:08:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/898",
    "number": "898",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "UNRWA Funding Emergency Restoration Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:08:28Z",
    "updateDateIncludingText": "2025-12-05T22:08:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T20:23:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-06",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MD"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MN"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s898is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 898\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Welch (for himself, Mr. Merkley , Mr. Sanders , Ms. Klobuchar , Mr. Van Hollen , Ms. Smith , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo restore funding for the United Nations Relief and Works Agency for Palestine Refugees in the Near East (UNRWA).\n#### 1. Short title\nThis Act may be cited as the UNRWA Funding Emergency Restoration Act of 2025 .\n#### 2. Statement of policy\nCongress\u2014\n**(1)**\nrecognizes that preventing further erosion of civilian conditions in Gaza remains in the strategic and moral interests of the United States;\n**(2)**\nsupports UNRWA\u2019s unique and indispensable contribution to immediately addressing urgent humanitarian needs in Gaza, especially in mitigating and stopping the spread of famine and disease;\n**(3)**\nreaffirms the imperative of UNRWA\u2019s continued provision of humanitarian and human development services to Palestinian refugees in all its current fields of operation, including Jordan, Lebanon, Syria, Gaza, and the West Bank (including East Jerusalem);\n**(4)**\nurges the Government of Israel to assist UNRWA in its neutrality efforts by providing names, information, and evidence UNRWA can use to aggressively pursue allegations related to staff violations of UNRWA\u2019s neutrality policies;\n**(5)**\nurges the President\u2014\n**(A)**\nto join United States allies in restoring funding to UNRWA in response to the responsible actions taken by the United Nations and the commitments made by UNRWA toward additional accountability and transparency; and\n**(B)**\nto ensure continued funding to UNRWA is assessed based on UNRWA\u2019s ongoing execution of the recommendations of the Independent Review Group, led by Catherine Colonna;\n**(6)**\nrecognizes the implementation of some of the Independent Review Group\u2019s recommendations will require United Nations member state cooperation, including additional funding;\n**(7)**\nurges the United States and Israel to assist UNRWA in its implementation efforts of the Independent Review Group\u2019s recommendations; and\n**(8)**\nsupports appropriating critical funds to UNRWA for fiscal year 2025 and beyond.\n#### 3. Restoration of funding for UNRWA\n##### (a) In general\nBeginning on the date of the enactment of this Act\u2014\n**(1)**\ntitle III of division G of the Further Consolidated Appropriations Act, 2024 ( Public Law 118\u201347 ) is hereby repealed;\n**(2)**\nsection 308 of the Israel Security Supplemental Appropriations Act, 2024 (division A of Public Law 118\u201350 ) is hereby repealed; and\n**(3)**\nthe Secretary of State shall, notwithstanding any other provision of law and as soon as practicable\u2014\n**(A)**\nresume the provision of funding to UNRWA under current authorities of the Department of State; and\n**(B)**\nprovide funding to UNRWA consistent with the Secretary\u2019s waiver for lifesaving humanitarian aid; and\n**(4)**\nthe President shall rescind the Executive order entitled \u2018\u2018Withdrawing the United States From and Ending Funding to Certain United Nations Organizations and Reviewing United States Support to All International Organizations\u2019\u2019 of February 4, 2025 (90 Fed. Reg. 9275).\n##### (b) Reports\nNot later than 90 days after the date of the enactment of this Act, and quarterly thereafter through December 31, 2028, the Secretary of State shall submit a report to the appropriate congressional committees of jurisdiction describing the steps UNRWA is taking to implement the recommendations made by the Independent Review Group, led by Catherine Colonna.",
      "versionDate": "2025-03-06",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "2411",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "UNRWA Funding Emergency Restoration Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-05-21T13:11:58Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s898is.xml"
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
      "title": "UNRWA Funding Emergency Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "UNRWA Funding Emergency Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restore funding for the United Nations Relief and Works Agency for Palestine Refugees in the Near East (UNRWA).",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:40Z"
    }
  ]
}
```
