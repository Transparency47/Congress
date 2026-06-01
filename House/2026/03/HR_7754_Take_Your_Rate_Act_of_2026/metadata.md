# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7754?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7754
- Title: Take Your Rate Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7754
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-04-21T17:43:31Z
- Update date including text: 2026-04-21T17:43:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7754",
    "number": "7754",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Take Your Rate Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-21T17:43:31Z",
    "updateDateIncludingText": "2026-04-21T17:43:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:02:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7754ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7754\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Barrett introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require a study on the feasibility and potential impacts of portable Federally backed mortgage loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Take Your Rate Act of 2026 .\n#### 2. Study on mortgage portability\n##### (a) In general\nThe Secretary of Housing and Urban Development and the Director of the Federal Housing Finance Agency shall jointly conduct a study on the feasibility and potential impacts of mortgage loan portability for Federally backed mortgage loans.\n##### (b) Required considerations\nThe study required under subsection (a) shall include an analysis of\u2014\n**(1)**\nadministrative and operational feasibility;\n**(2)**\nthe effect on the housing market if Federally backed mortgage loans were portable;\n**(3)**\nany changes to rulemaking and regulations at the Department of Housing and Urban Development and the Federal Housing Finance Agency to allow such mortgages to become portable;\n**(4)**\nhow many current borrowers would benefit from such portable mortgages;\n**(5)**\nthe budgetary impact that such portable mortgages would have on the Federal Government;\n**(6)**\nthe financial safety and soundness implications for federally backed mortgage programs and the Federal National Mortgage Association and the Federal Home Loan Mortgage Corporation if such mortgages were portable;\n**(7)**\nany statutory changes needed, if any;\n**(8)**\nrecommendations on whether a limited demonstration program would be beneficial and how it should be administered;\n**(9)**\nany other information the Secretary of Housing and Urban Development and the Director of the Federal Housing Finance Agency finds important to include; and\n**(10)**\nif the Secretary and Director determines that it is not feasible, recommendations regarding similar solutions or alternative program designs that could be administered to provide relief on the housing market.\n##### (c) Consultation\nThe Secretary of Housing and Urban Development and the Director of the Federal Housing Finance Agency may consult with the following entities if it would be beneficial for the study and report:\n**(1)**\nThe Federal National Mortgage Association.\n**(2)**\nThe Federal Home Loan Mortgage Corporation.\n**(3)**\nThe Federal Housing Administration.\n**(4)**\nThe Department of Veterans Affairs.\n**(5)**\nThe Department of Agriculture.\n**(6)**\nMortgage lenders and servicers.\n**(7)**\nAny other Federal agencies, departments, or outside industries that it sees as beneficial.\n##### (d) Federally backed mortgage loan defined\nIn this Act, The term Federally backed mortgage loan means any loan (other than temporary financing such as a construction loan) that\u2014\n**(1)**\nis secured by a first or subordinate lien on residential real property (including individual units of condominiums and cooperatives) designed principally for the occupancy of 1 to 4 families, including any such secured loan, the proceeds of which are used to prepay or pay off an existing loan secured by the same property; and\n**(2)**\nis made in whole or in part, or insured, guaranteed, supplemented, or assisted in any way, by any officer or agency of the Federal Government or under or in connection with a housing or urban development program administered by the Secretary of Housing and Urban Development or a housing or related program administered by any other such officer or agency, or is purchased or securitized by the Federal Home Loan Mortgage Corporation or the Federal National Mortgage Association.\n#### 3. Report to Congress\nNot later than 180 days after the date of enactment of this Act, the Secretary and the Director shall submit to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate a joint report containing\u2014\n**(1)**\nthe findings of the study required under section 2;\n**(2)**\npolicy recommendations, if any;\n**(3)**\nan assessment of risks and benefits to taxpayers and financial markets; and\n**(4)**\nany dissenting views from either agency.",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-04-21T17:43:30Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7754ih.xml"
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
      "title": "Take Your Rate Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T08:23:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Take Your Rate Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T08:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a study on the feasibility and potential impacts of portable Federally backed mortgage loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T08:18:46Z"
    }
  ]
}
```
