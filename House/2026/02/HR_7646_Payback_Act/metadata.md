# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7646
- Title: Payback Act
- Congress: 119
- Bill type: HR
- Bill number: 7646
- Origin chamber: House
- Introduced date: 2026-02-23
- Update date: 2026-03-12T20:08:07Z
- Update date including text: 2026-03-12T20:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-23: Introduced in House

## Actions

- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-23",
    "latestAction": {
      "actionDate": "2026-02-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7646",
    "number": "7646",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Payback Act",
    "type": "HR",
    "updateDate": "2026-03-12T20:08:07Z",
    "updateDateIncludingText": "2026-03-12T20:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-23",
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
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-23",
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
          "date": "2026-02-23T17:01:40Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7646ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7646\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 23, 2026 Ms. Crockett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo direct the Secretary of the United States Department of the Treasury to refund American consumers for increased costs resulting from tariffs imposed without congressional authorization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Payback Act .\n#### 2. Congressional findings\nCongress finds the following:\n**(1)**\nIn Learning Resources, Inc. v. Trump, the Supreme Court of the United States clarified that although the International Emergency Economic Powers Act authorizes the President to exercise certain economic authorities during a bona fide national emergency, that statute does not confer authority to impose tariffs absent clear and express congressional authorization; in so holding, the Court reaffirmed that article I, section 8 of the Constitution vests exclusively in Congress the power to lay and collect duties and tariffs, and that such legislative authority may not be exercised by the executive branch solely by virtue of an emergency declaration.\n**(2)**\nThe Constitution establishes a deliberate separation of powers, vesting in Congress alone the authority to lay and collect taxes, duties, imposts, and excises under article I, section 8; allowing the executive branch to unilaterally impose tariffs absent explicit congressional authorization would improperly transfer core legislative power to the Presidency, erode democratic accountability, and undermine the foundational principle that laws affecting the economic lives of Americans must originate with the people\u2019s elected representatives.\n**(3)**\nThese unlawful tariffs resulted in billions of dollars in collections by the Federal Government and materially increased the prices of goods for American consumers, functioning as a regressive tax that disproportionately burdened working families, seniors, and small businesses.\n**(4)**\nAmerican consumers bore the direct financial consequences of these actions through higher costs on everyday necessities, without meaningful notice, representation, or recourse, and shall be made whole through a transparent and congressionally directed refund process administered by the Federal Government.\n#### 3. Definitions\nIn this Act:\n**(1) Covered tariffs**\nThe term covered tariffs means any duties or fees imposed pursuant to Presidential proclamations or Executive orders under the International Emergency Economic Powers Act that were subsequently determined to lack congressional authorization.\n#### 4. Establishment of consumer refund formula\n##### (a)\nNot later than 120 days after enactment of this Act, the Secretary of the Treasury shall develop and publish a formula to calculate refunds to American consumers for amounts paid that were attributable to covered tariffs.\n##### (b)\nThe refund formula shall\u2014\n**(1)**\nquantify total consumer cost increases tied to covered tariffs using data from U.S. Customs and Border Protection, the Bureau of Economic Analysis, and other relevant Federal datasets;\n**(2)**\nestimate pass-through effects from importers, distributors, and retailers to end consumers; and\n**(3)**\nincorporate equitable adjustments based on household income and geographic disparities.\n##### (c) Consultation\nIn developing the formula, the Secretary shall consult with the Bureau of Economic Analysis, the Internal Revenue Service, the Federal Reserve Board, and independent economists with expertise in trade policy and consumer pricing.\n#### 5. Distribution of refunds\n##### (a)\nTo the maximum extent practicable, refunds shall be issued automatically using existing Treasury and Internal Revenue Service payment systems, including direct deposit or refundable tax credits.\n##### (b)\nFor individuals not captured through existing systems, the Secretary shall establish a streamlined application process requiring minimal documentation.\n#### 6. Report to Congress and oversight\nNot later than 180 days after enactment, the Secretary shall submit a report to Congress detailing the finalized refund formula, total anticipated refund obligations, and projected distribution timelines. The Government Accountability Office shall review the implementation of this Act and submit findings to Congress not later than one year after refunds commence.",
      "versionDate": "2026-02-23",
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
        "updateDate": "2026-03-12T20:08:06Z"
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
      "date": "2026-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7646ih.xml"
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
      "title": "Payback Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T03:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Payback Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-11T03:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the United States Department of the Treasury to refund American consumers for increased costs resulting from tariffs imposed without congressional authorization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-11T03:33:38Z"
    }
  ]
}
```
