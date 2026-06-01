# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4803
- Title: Easy Returns Act
- Congress: 119
- Bill type: HR
- Bill number: 4803
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2025-09-12T18:40:49Z
- Update date including text: 2025-09-12T18:40:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4803",
    "number": "4803",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "J000310",
        "district": "32",
        "firstName": "Julie",
        "fullName": "Rep. Johnson, Julie [D-TX-32]",
        "lastName": "Johnson",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Easy Returns Act",
    "type": "HR",
    "updateDate": "2025-09-12T18:40:49Z",
    "updateDateIncludingText": "2025-09-12T18:40:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:06:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4803ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4803\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Ms. Johnson of Texas introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require certain sellers of goods to provide return labels as part of the delivery of such goods, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Easy Returns Act .\n#### 2. Provision of return labels\n##### (a) Requirement\nNo person described in subsection (b) may sell to a consumer a physical good that requires subsequent delivery to such consumer without including, as part of such delivery, a physical label appropriately addressed for purposes of the return of such good.\n##### (b) Covered persons\nA person is described in this subsection if such person employed, in the preceding year, at least 500 employees.\n##### (c) Limitations\nSubsection (a) does not apply with respect to the sale of a physical good\u2014\n**(1)**\nthat is perishable and not typically returned by a consumer after delivery;\n**(2)**\nthat is custom made or personalized in a manner that prevents resale to another consumer if returned; or\n**(3)**\nwith respect to which the person selling the good offers an accessible and convenient return method other than return by means of shipping, including a scheduled, at-home pickup service that is available without cost to a consumer.\n##### (d) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Federal Trade Commission shall promulgate, under section 553 of title 5, United States Code, regulations to carry out this section.\n##### (e) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section or a regulation promulgated under this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Federal Trade Commission shall enforce this section and the regulations promulgated under this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section. Any person who violates this section or a regulation promulgated under this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (f) Applicability\nThis section shall apply to sales occurring on or after the date that is 1 year after the date of the enactment of this Act.\n##### (g) Rule of construction\nNothing in this section may be construed to limit any right or remedy available to a consumer under any other provision of law.",
      "versionDate": "2025-07-29",
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
        "name": "Commerce",
        "updateDate": "2025-09-12T18:40:49Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4803ih.xml"
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
      "title": "Easy Returns Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Easy Returns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require certain sellers of goods to provide return labels as part of the delivery of such goods, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T07:48:48Z"
    }
  ]
}
```
