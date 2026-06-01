# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7842?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7842
- Title: Alien Banking Act
- Congress: 119
- Bill type: HR
- Bill number: 7842
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-04-01T16:34:30Z
- Update date including text: 2026-04-01T16:34:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7842",
    "number": "7842",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Alien Banking Act",
    "type": "HR",
    "updateDate": "2026-04-01T16:34:30Z",
    "updateDateIncludingText": "2026-04-01T16:34:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7842ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7842\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Ogles (for himself, Mr. Crane , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend section 5318 of title 31, United States Code, to require financial institutions to verify the lawful immigration status of applicants for deposit accounts through a self-attestation form, to impose penalties on individuals for false attestations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Alien Banking Act .\n#### 2. Requirement for immigration status verification in customer identification programs\n##### (a) In general\nSection 5318(l) of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (B), by striking and at the end;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(D) requiring any individual who is present in the United States and seeking to open an account to attest, under penalty of perjury, to the individual\u2019s lawful presence in the United States, including by checking a box or similar affirmation on the deposit account application form indicating whether the individual is a United States citizen, a lawful permanent resident, or otherwise lawfully present in the United States, as defined by the Secretary of Homeland Security in consultation with the Secretary of the Treasury. ; and\n**(2)**\nby adding at the end the following:\n(7) Prohibition on opening accounts for unlawfully present individuals A financial institution may not open or maintain an account for any individual who fails to provide the attestation required under paragraph (2)(D). (8) Penalties for individuals (A) Civil penalty Any individual who knowingly makes a false attestation described in paragraph (2)(D) is liable for a civil penalty of not less than $10,000 and not more than $50,000. (B) Criminal penalty Any individual who knowingly makes a false attestation described in paragraph (2)(D) shall be fined under title 18, United States Code, imprisoned not more than 5 years, or both. Notwithstanding title 18, United States Code, the fine under this subparagraph shall not exceed $250,000. (C) Forfeiture of assets (i) Civil forfeiture In the case of an individual knowingly making a false attestation described in paragraph (2)(D) in connection with an account, any property contained in the account, regardless of when such property was placed in the account, and any property otherwise traceable to the account, may be seized and forfeited to the United States in accordance with the procedures governing civil forfeitures in money laundering cases pursuant to section 981(a)(1)(A) of title 18, United States Code. (ii) Criminal forfeiture (I) In general A court, in imposing sentence for an individual knowingly making a false attestation described in paragraph (2)(D) in connection with an account, shall order the defendant to forfeit all property contained in the account, regardless of when such property was placed in the account, and any property otherwise traceable to the account. (II) Procedure Forfeitures under this clause shall be governed by the procedures established in section 413 of the Controlled Substances Act. (9) Reporting requirement A financial institution that has reason to believe an individual has made a false attestation described in paragraph (2)(D) shall report such belief to the Secretary of Homeland Security and the Attorney General. .\n#### 3. Regulations\nNot later than 180 days after the date of enactment of this Act, the Secretary of the Treasury, in consultation with the Secretary of Homeland Security and the Attorney General, shall issue regulations to implement the amendments made by section 2 of this Act, including\u2014\n**(1)**\nmodel language for the attestation described in 5318(l)(2)(D) of title 31, United States Code; and\n**(2)**\nguidelines for reporting suspected false attestations under section 5318(l)(9) of such title.\n#### 4. Effective date\nThe provisions added by the amendments made by this Act shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2026-03-05",
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
        "name": "Immigration",
        "updateDate": "2026-04-01T16:34:30Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7842ih.xml"
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
      "title": "Alien Banking Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T02:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Alien Banking Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 5318 of title 31, United States Code, to require financial institutions to verify the lawful immigration status of applicants for deposit accounts through a self-attestation form, to impose penalties on individuals for false attestations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:22Z"
    }
  ]
}
```
