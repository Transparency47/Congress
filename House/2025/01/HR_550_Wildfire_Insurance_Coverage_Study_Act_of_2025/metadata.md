# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/550?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/550
- Title: Wildfire Insurance Coverage Study Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 550
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-09-17T15:09:39Z
- Update date including text: 2025-09-17T15:09:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/550",
    "number": "550",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Wildfire Insurance Coverage Study Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-17T15:09:39Z",
    "updateDateIncludingText": "2025-09-17T15:09:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:00:50Z",
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr550ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 550\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Ms. Waters (for herself and Mr. Sherman ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Government Accountability Office to conduct a study regarding insurance coverage for damages from wildfires, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Insurance Coverage Study Act of 2025 .\n#### 2. GAO study regarding insurance for wildfire damage\n##### (a) Study\nThe Comptroller General of the United States, in consultation with the Director of the Federal Insurance Office and State insurance regulators, shall conduct a study to analyze and determine the following:\n**(1) Risk assessment**\nThe extent and nature of wildfire risk in the United States, including\u2014\n**(A)**\nidentifying trends in declarations for wildfires under the Fire Management Assistance grant program under section 420 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5187 ), with respect to geography, costs, probability, and frequency of wildfire disasters;\n**(B)**\nidentifying mitigation practices that would assist in reducing costs and risks for insurance policies covering damages from wildfires;\n**(C)**\nidentifying existing programs of the Federal Government and State governments that measure wildfire risk and assess their effectiveness in forecasting wildfire events and informing wildfire response; and\n**(D)**\nanalyzing and assessing the need for a national map for measuring and quantifying wildfire risk.\n**(2) Existing state of coverage**\nWith respect to the existing state of homeowners insurance coverage and commercial property insurance coverage for damage from wildfires in the United States\u2014\n**(A)**\nthe extent to which private insurers have, during the 10-year period ending on the date of the enactment of this Act, adjusted rates, policyholder cost-sharing provisions, or both for such coverage (after adjusting for inflation) and the geographic areas in which adjusted rates, policyholder cost-sharing, or both have increased;\n**(B)**\nthe extent to which private insurers have, during the 10-year period ending on the date of the enactment of this Act, declined to renew policies for such coverages and the geographic areas to which such declinations applied;\n**(C)**\nthe events and economic factors that have contributed to any such increased rates and declinations to renew policies;\n**(D)**\nin cases in which private insurers have curtailed their overall wildfire exposure, the extent to which homeowners insurance coverage and commercial property coverage were terminated altogether and the extent to which such coverages are still offered but with coverage for damage from wildfires excluded; and\n**(E)**\nthe extent to which, and circumstances under which, private insurers are continuing to provide coverage for damage from wildfires\u2014\n**(i)**\nin general;\n**(ii)**\nsubject to a condition that mitigation activities are taken, such as hardening of properties and landscaping against wildfires, by property owners, State or local governments, park or forest authorities, or other land management authorities; and\n**(iii)**\nsubject to any other conditions.\n**(3) Regulatory responses**\nWith respect to actions taken by State insurance regulatory agencies in response to increased premium rates, policyholder cost-sharing, or both for coverage for damage from wildfires or exclusion of such coverage from homeowners insurance policies\u2014\n**(A)**\nthe extent to which States have leveraged their respective authorities to regulate rate increases;\n**(B)**\nthe extent to which States have enacted any moratoria on such rate and policyholder cost-sharing increases or exclusions and on non-renewals;\n**(C)**\nthe extent to which States require homeowners insurance coverage to include coverage for damage from wildfires or make sales of homeowners insurance coverage contingent on the sale, underwriting, or financing of separate wildfire coverage in the State;\n**(D)**\nthe extent to which States have established State residual market insurance entities, reinsurance programs, or similar mechanisms for coverage of damages from wildfires;\n**(E)**\nany other actions States or localities have taken in response to increased premium rates, policyholder cost-sharing, or both for coverage for damage from wildfires or exclusion of such coverage from homeowners policies, including forestry and wildfire management policies and subsidies for premiums and cost-sharing for wildfire coverage;\n**(F)**\nthe effects of actions taken by States on the availability, coverage level, and affordability of homeowners insurance coverage; and\n**(G)**\nthe effectiveness and sustainability of such actions taken by States.\n**(4) Challenges in underwriting wildfire risk**\nWith respect to the challenges faced by private insurers underwriting wildfire risk, what is or are\u2014\n**(A)**\nthe correlated risks and the extent of such risks;\n**(B)**\nthe factors affecting the extent of private insurers\u2019 ability to estimate magnitude of future likelihood of wildfires and of expected damages from wildfires;\n**(C)**\nthe effects of the need to increase more affordable housing options, which may contribute to increased homebuilding in more remote, heavily-wooded areas with higher wildfire risk;\n**(D)**\nthe potential for wildfire losses sufficiently large to jeopardize insurers\u2019 solvency;\n**(E)**\nthe extent to which, and areas in which, risk-adjusted market premiums for wildfire risk limit affordability or availability of coverage for consumers;\n**(F)**\nthe effects of various existing and potential State and Federal Government responses to help address these challenges and mitigate wildfire risk, including actions such as\u2014\n**(i)**\nimproved forest management policies;\n**(ii)**\nimproved data to estimate risk;\n**(iii)**\nrelocating homeowners from wildfire zones;\n**(iv)**\noffsetting a portion of insurers\u2019 charged risk-adjusted premiums with means-tested government affordability programs for lower income homeowners;\n**(v)**\nencouraging the increased use of private reinsurance and other risk-sharing mechanisms by insurers to better diversify wildfire risk; and\n**(vi)**\ndeveloping programs that offset the costs of wildfire risk for consumers and industry;\n**(G)**\nthe available policy responses if private insurers exit the wildfire coverage market and the potential advantages and disadvantages of each such response;\n**(H)**\nthe effects of the availability and affordability of wildfire coverage, policyholder cost-sharing, or both, on\u2014\n**(i)**\nlocal communities that are disproportionately vulnerable to wildfires, including on low- or moderate-income property owners and small businesses;\n**(ii)**\nrebuilding in communities previously damaged by wildfires;\n**(iii)**\nthe availability and affordability of housing supply; and\n**(iv)**\nthe demand for wildfire insurance coverage by property owners;\n**(I)**\nthe effects of potential State prohibitions on termination of policies due to wildfire claims on insurer solvency; and\n**(J)**\nthe manner in which private insurers are modeling or estimating future wildfire risk.\n##### (b) Report\nNot later than the expiration of the 12-month period beginning on the date of the enactment of this Act, the Comptroller General shall submit to the Congress a report identifying the findings and conclusions of the study conducted pursuant to subsection (a).",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2430",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Wildfire Insurance Coverage Study Act of 2025",
      "type": "S"
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
        "updateDate": "2025-02-18T20:58:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr550",
          "measure-number": "550",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr550v00",
            "update-date": "2025-04-15"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Wildfire Insurance Coverage Study Act of 2025 </strong></p><p>This bill requires reports regarding wildfire risk and damage. Specifically, the Government Accountability Office (GAO)\u00a0must report on trends in wildfire declarations, mitigation practices, state and federal programs regarding wildfire risk, and the need for a national map of wildfire risks.</p><p>The GAO must also report on (1) the availability and cost of wildfire insurance coverage for homes and commercial property, (2) state regulatory responses to increasing costs of coverage, and (3) impediments to private wildfire insurance coverage.</p>"
        },
        "title": "Wildfire Insurance Coverage Study Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr550.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Insurance Coverage Study Act of 2025 </strong></p><p>This bill requires reports regarding wildfire risk and damage. Specifically, the Government Accountability Office (GAO)\u00a0must report on trends in wildfire declarations, mitigation practices, state and federal programs regarding wildfire risk, and the need for a national map of wildfire risks.</p><p>The GAO must also report on (1) the availability and cost of wildfire insurance coverage for homes and commercial property, (2) state regulatory responses to increasing costs of coverage, and (3) impediments to private wildfire insurance coverage.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119hr550"
    },
    "title": "Wildfire Insurance Coverage Study Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wildfire Insurance Coverage Study Act of 2025 </strong></p><p>This bill requires reports regarding wildfire risk and damage. Specifically, the Government Accountability Office (GAO)\u00a0must report on trends in wildfire declarations, mitigation practices, state and federal programs regarding wildfire risk, and the need for a national map of wildfire risks.</p><p>The GAO must also report on (1) the availability and cost of wildfire insurance coverage for homes and commercial property, (2) state regulatory responses to increasing costs of coverage, and (3) impediments to private wildfire insurance coverage.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119hr550"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr550ih.xml"
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
      "title": "Wildfire Insurance Coverage Study Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Insurance Coverage Study Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Government Accountability Office to conduct a study regarding insurance coverage for damages from wildfires, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:18Z"
    }
  ]
}
```
