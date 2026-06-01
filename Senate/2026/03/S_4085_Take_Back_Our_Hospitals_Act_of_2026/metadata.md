# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4085?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4085
- Title: Take Back Our Hospitals Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4085
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-02T18:28:55Z
- Update date including text: 2026-04-02T18:28:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4085",
    "number": "4085",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Take Back Our Hospitals Act of 2026",
    "type": "S",
    "updateDate": "2026-04-02T18:28:55Z",
    "updateDateIncludingText": "2026-04-02T18:28:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T17:31:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4085is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4085\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Murphy (for himself, Mr. Blumenthal , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to prevent hospitals or skilled nursing facilities that are owned by certain firms from participating in the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Take Back Our Hospitals Act of 2026 .\n#### 2. Preventing hospitals and skilled nursing facilities owned by certain firms from participating in Medicare\nSection 1862 of the Social Security Act ( 42 U.S.C. 1395y ) is amended by adding at the end the following new subsection:\n(p) Prohibition on payments to hospitals and skilled nursing facilities owned by certain firms (1) In general (A) Prohibition No payment may be made under this title to a hospital or skilled nursing facility that is owned or controlled by a covered firm or an affiliate of a covered firm. (B) Exception If, on the date of enactment of this subsection, a hospital or skilled nursing facility is owned or controlled by a covered firm or an affiliate of such a firm, such hospital or skilled nursing facility shall not be considered in violation of subparagraph (A) until the date that is 3 years after such date of enactment. (2) Notice, hearing, and judicial review Any hospital or skilled nursing facility found to be in violation of paragraph (1) shall be entitled to reasonable notice and opportunity for hearing as described in section 1128(f). (3) Joint and several liability A covered firm or an affiliate of such a firm that owns or is an affiliate of a hospital or skilled nursing facility that is in violation of paragraph (1) shall be jointly and severally liable for any penalty or obligation such hospital or skilled nursing facility receives for such violation. (4) Definitions In this subsection: (A) Affiliate The term affiliate means an entity that controls, is controlled by, or is under common control with another entity. (B) Control (i) In general The term control means to possess the power, directly or indirectly, to direct, or cause the direction of, the management, administrative functions, assets, or policies of an entity through owning voting securities in such entity, contracting with such entity (except for contracting with such entity for goods or non-management services), or other similar means, as determined by the Secretary. (ii) Voting securities A person shall be considered to control an entity if such person directly or indirectly owns, has rights over, or holds with the power to vote, 10 percent or more of the voting securities of such entity. (C) Corporation The term corporation means\u2014 (i) a joint-stock company; (ii) a company or partnership association organized under a law that makes only the capital subscribed or callable up to a specified amount responsible for the debts of the company or partnership association, and includes a limited partnership and a limited liability company; (iii) a trust; or (iv) an association that\u2014 (I) possesses the power or privilege of a private corporation under State law; and (II) does not possess the power or privilege of a sole proprietorship or partnership under State law. (D) Covered firm The term covered firm means\u2014 (i) a private equity fund; (ii) a corporation that is owned or controlled by a private equity fund; or (iii) a real estate investment trust. (E) Private equity fund The term private equity fund means a person who\u2014 (i) would be considered an investment company under section 3 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20133 ) but for the application of paragraph (1) or (7) of subsection (c) of such section; and (ii) directly, or through an affiliate, acts as a control person of such company. (F) Real estate investment trust The term real estate investment trust has the meaning given such term in section 856 of the Internal Revenue Code of 1986. .",
      "versionDate": "2026-03-12",
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
        "actionDate": "2026-03-12",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7920",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Take Back Our Hospitals Act of 2026",
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
        "name": "Health",
        "updateDate": "2026-04-02T18:28:37Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4085is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to prevent hospitals or skilled nursing facilities that are owned by certain firms from participating in the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:26Z"
    },
    {
      "title": "Take Back Our Hospitals Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Take Back Our Hospitals Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
