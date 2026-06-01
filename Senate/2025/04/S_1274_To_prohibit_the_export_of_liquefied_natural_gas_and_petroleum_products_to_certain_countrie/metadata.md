# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1274
- Title: Protecting American Households From Rising Energy Costs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1274
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2025-05-02T10:39:09Z
- Update date including text: 2025-05-02T10:39:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1274",
    "number": "1274",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Protecting American Households From Rising Energy Costs Act of 2025",
    "type": "S",
    "updateDate": "2025-05-02T10:39:09Z",
    "updateDateIncludingText": "2025-05-02T10:39:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:27:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "RI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-03",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1274is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1274\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Merkley (for himself, Mr. Reed , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit the export of liquefied natural gas and petroleum products to certain countries.\n#### 1. Short title\nThis Act may be cited as the Protecting American Households From Rising Energy Costs Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Petroleum product**\nThe term petroleum product has the meaning given the term in section 3 of the Energy Policy and Conservation Act ( 42 U.S.C. 6202 ).\n**(2) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Prohibition on exports of liquefied natural gas and petroleum products to certain countries\n##### (a) Prohibitions\n**(1) In general**\nNotwithstanding any other provision of law, unless a waiver has been issued under subsection (b), no person or entity may export or resell, either directly or indirectly through 1 or more third parties, liquefied natural gas or petroleum products\u2014\n**(A)**\nto any entity operating in the territory of, or territory owned by, the People\u2019s Republic of China (or the Chinese Communist Party), the Russian Federation, the Democratic People\u2019s Republic of Korea, or the Islamic Republic of Iran; or\n**(B)**\nto any entity that is under the ownership or control, as determined by the Secretary in consultation with the Secretary of the Treasury and the Secretary of Commerce, of the People\u2019s Republic of China (or the Chinese Communist Party), the Russian Federation, the Democratic People\u2019s Republic of Korea, or the Islamic Republic of Iran.\n**(2) Responsibility**\nIt is the responsibility of the export authorization holder to ensure compliance with this Act and any other applicable law or policy, including rules, regulations, orders, and other determinations made by\u2014\n**(A)**\nthe Office of Foreign Assets Control of the Department of the Treasury; and\n**(B)**\nthe Federal Energy Regulatory Commission.\n##### (b) Waiver\n**(1) In general**\nOn application by an exporter, the Secretary may waive, prior to the date of the applicable contract, the prohibitions described in subsection (a) with respect to the sale of liquefied natural gas or petroleum products.\n**(2) Requirement**\nThe Secretary may issue a waiver under this subsection only if the Secretary determines that an imminent and acute national security emergency to the United States exists and that other means of responding to the emergency would be inadequate.\n**(3) Applications**\nAn exporter seeking a waiver under this subsection shall submit to the Secretary an application by such date, in such form, and containing such information as the Secretary may require.\n**(4) Notice to Congress**\nNot later than 15 days after issuing a waiver under this subsection, the Secretary shall provide a copy of the waiver to the Committee on Energy and Natural Resources of the Senate and the Committee on Energy and Commerce of the House of Representatives.\n##### (c) Rulemaking\nThe Secretary may promulgate, amend, and rescind rules and regulations, as the Secretary determines to be appropriate, to carry out this Act.\n#### 4. Enforcement provisions\n##### (a) Unlawful acts\nIt shall be unlawful for a person to violate, attempt to violate, conspire to violate, or cause a violation of any prohibition of, or any waiver, license, order, or regulation issued pursuant to this Act.\n##### (b) Civil penalty\n**(1) In general**\nThe Secretary may impose a civil penalty on any person who commits an unlawful act described in subsection (a) in an amount not to exceed the greater of\u2014\n**(A)**\n$250,000,000; and\n**(B)**\nan amount that is twice the amount of the transaction that is the basis of the violation with respect to which the penalty is imposed.\n**(2) Notice and opportunity for hearing**\nA civil penalty under paragraph (1) may be imposed by the Secretary by an order made on the record after providing written notice to the person to be assessed the civil penalty and an opportunity for a hearing in accordance with this section and sections 554 through 557 of title 5, United States Code.\n**(3) Civil action**\nIf a person described in paragraph (1) fails to pay a civil penalty imposed by the Secretary under this subsection after receiving notice and an opportunity for a hearing under paragraph (2), the Secretary may bring a civil action against that person in an appropriate district court of the United States.\n**(4) Relief**\nIf a civil action brought by the Secretary under paragraph (3) is successful, the applicable court may grant appropriate relief, including\u2014\n**(A)**\na temporary injunction;\n**(B)**\na permanent injunction; and\n**(C)**\nenforcing the civil penalties described in paragraph (1).\n##### (c) Criminal penalty\nA person who knowingly commits, knowingly attempts to commit, or knowingly conspires to commit, or aids or abets in the commission of, an unlawful act described in subsection (a) shall be fined not more than $100,000,000, imprisoned for not more than 20 years, or both.",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
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
        "name": "Energy",
        "updateDate": "2025-05-02T10:39:09Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1274is.xml"
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
      "title": "Protecting American Households From Rising Energy Costs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting American Households From Rising Energy Costs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the export of liquified natural gas and petroleum products to certain countries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:19:08Z"
    }
  ]
}
```
