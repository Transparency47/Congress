# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4489?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4489
- Title: Sunshine on Solar Lending Act
- Congress: 119
- Bill type: HR
- Bill number: 4489
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-11-18T09:05:41Z
- Update date including text: 2025-11-18T09:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4489",
    "number": "4489",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001091",
        "district": "20",
        "firstName": "Joaquin",
        "fullName": "Rep. Castro, Joaquin [D-TX-20]",
        "lastName": "Castro",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Sunshine on Solar Lending Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:41Z",
    "updateDateIncludingText": "2025-11-18T09:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:02:00Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "DC"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4489ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4489\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Castro of Texas (for himself and Ms. Norton ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Truth in Lending Act to require certain creditors to disclose dealer fees in solar financing transactions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sunshine on Solar Lending Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nHomeowners are increasingly installing solar energy systems, including battery storage systems and other related systems, to reduce electricity costs and maintain power during grid outages.\n**(2)**\nThe high upfront cost of purchasing and installing solar energy systems often requires consumers to obtain financing, typically through loans or leases facilitated by solar installers and originated by third-party creditors.\n**(3)**\nSolar financing arrangements are frequently marketed by third-party sales representatives or installers who partner with creditors to offer loans at the point of sale. In some cases, these arrangements include dealer fees that are not clearly disclosed to consumers, leading to inflated financing costs and a lack of transparency regarding the true cost of credit.\n**(4)**\nThe Seller\u2019s Point exemption under Regulation Z is sometimes improperly used to exclude dealer fees from the calculation of the finance charge in solar financing transactions. The use of this exemption has led to confusion and inconsistent treatment of such fees, particularly in transactions involving third-party financing and indirect compensation structures.\n**(5)**\nThe Truth in Lending Act applies to creditors, as defined in the Act, that offer or extend credit for solar energy systems. All such creditors are required to comply with the disclosure and consumer protection provisions of the Act.\n**(6)**\nThis Act is necessary to clarify and reinforce the application of the Truth in Lending Act to solar financing transactions, ensure consistent treatment of dealer fees as finance charges where applicable, and promote transparency and accountability in credit transactions related to solar energy systems.\n#### 3. Disclosure of dealer fees in solar financing transactions\nSection 106 of the Truth in Lending Act ( 15 U.S.C. 1605 ) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(7) in any consumer credit transaction for solar financing, as defined in subsection (h), any seller\u2019s points or other charges imposed by the creditor upon a noncreditor seller for providing credit to the consumer or for providing credit on certain terms. ; and\n**(2)**\nby adding at the end the following:\n(g) Disclosure of dealer fees for solar financing transactions (1) In general A creditor for a solar financing transaction shall clearly and conspicuously disclose in writing to the consumer\u2014 (A) any fee charged to a third party by the creditor relating to the solar financing transaction; (B) any fee imposed directly or indirectly by the creditor or a third party, that is payable directly or indirectly by the consumer, relating to the solar financing transaction; (C) the identification of any third party that is a party to the solar financing transaction; and (D) a comparison of the amount financed by the solar financing transaction, including the amount of any finance charges with\u2014 (i) the total cash price for each product obtained by the consumer through the solar financing transaction, including infrastructure and labor costs; and (ii) the total cash price for each service obtained by the consumer through the solar financing transaction, including maintenance and repair costs. (2) In-person transactions With respect to a solar financing transaction negotiated (in part or in whole) with the consumer in person, a creditor or third party (as applicable) shall provide the consumer with a paper copy of the disclosures described in paragraph (1). (3) Arbitration A solar financing transaction may not include terms which require arbitration or any other nonjudicial procedure as the method for resolving any controversy or settling any claims arising out of the transaction. (h) Solar financing transaction defined In this section, the term solar financing transaction means a consumer credit transaction to finance the purchase, installation, or associated costs of a solar energy system, including solar panels, inverters, battery storage systems, electric vehicle charging stations, and any related infrastructure required for the operation of such solar energy system. .\n#### 4. Effective date; applicability\nThis Act and the amendments made by this Act shall take effect not later than 60 days after the date of the enactment of this Act and shall apply with respect to a solar financing transaction (as defined in subsection (h) of section 106 of the Truth in Lending Act ( 15 U.S.C. 1605 ), as added by this Act) entered into on or after such effective date.",
      "versionDate": "2025-07-17",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-11T15:42:51Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4489ih.xml"
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
      "title": "Sunshine on Solar Lending Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sunshine on Solar Lending Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Truth in Lending Act to require certain creditors to disclose dealer fees in solar financing transactions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:34Z"
    }
  ]
}
```
