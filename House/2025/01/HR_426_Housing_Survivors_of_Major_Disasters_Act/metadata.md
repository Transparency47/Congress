# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/426?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/426
- Title: Housing Survivors of Major Disasters Act
- Congress: 119
- Bill type: HR
- Bill number: 426
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-10T09:06:17Z
- Update date including text: 2025-12-10T09:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-15 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/426",
    "number": "426",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Housing Survivors of Major Disasters Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:06:17Z",
    "updateDateIncludingText": "2025-12-10T09:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-16T15:36:13Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-15T15:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr426ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 426\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Espaillat (for himself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo make available necessary disaster assistance for families affected by major disasters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Survivors of Major Disasters Act .\n#### 2. Definitions\nIn this Act:\n**(1) FEMA**\nThe term FEMA means the Federal Emergency Management Agency.\n**(2) Administrator**\nThe term Administrator means the Administrator of FEMA.\n#### 3. Eligibility for and use of disaster assistance\n##### (a) Evidence\n**(1) Consideration**\nWhere an individual or household does not have documented ownership rights in their predisaster primary residence, in making a determination to provide assistance pursuant to paragraphs (2) and (3) of section 408(c) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(c) ), the President shall consider an individual or household claim to having constructive ownership where evidence supports that it is more likely than not the individual or household has such ownership.\n**(2) Forms of evidence**\nIn determining whether it is more likely than not that an individual or household has constructive ownership under paragraph (1), the Administrator shall consider all evidence provided by an individual or household, including a digital or physical copy of the following:\n**(A)**\nThe deed or title for the applicable property.\n**(B)**\nA mortgage payment booklet or another mortgage document.\n**(C)**\nProperty title of mobile home certificate of title.\n**(D)**\nA real estate property tax receipt.\n**(E)**\nA will and testament with the name and address of the individual that conveys the individual is the owner.\n**(F)**\nIn a State that does not require a will and testament for the transfer of immovable property, a death certificate and birth certificate that establishes an automatic transfer of legal ownership.\n**(G)**\nHomeowners insurance documentation.\n**(H)**\nHome Purchase Contracts, including, but not limited to, Bill of Sale, Bond for Title, Land Installment Contracts.\n**(I)**\nReceipts of major repairs or maintenance dated within five years prior to the disaster.\n**(J)**\nCourt Documents.\n**(K)**\nLetter prepared after the disaster from a mobile home park owner or manager or public office that meets FEMA requirements.\n**(L)**\nNotice of Federal benefits.\n**(M)**\nStudent loan documentation.\n**(N)**\nAny other documentation, certification, identification, or proof of occupancy or ownership not included on this list that can reasonably link the individual requesting assistance to the applicable property, as determined by the President.\n**(3) Declarative statement**\n**(A) In general**\nWhere evidence of constructive ownership is not sufficient, the Administrator may require the individual or household to provide a declarative statement, signed under penalty of perjury, that describes why the individual or household is the constructive owner of the property.\n**(B) Prohibition of notarization**\nThe Administrator may not require notarization of a declarative statement submitted under this paragraph.\n##### (b) Definition of constructive ownership\nIn this section, the term constructive ownership means that an individual\u2019s or household\u2019s residence is owner-occupied, as determined by the Administrator, the purposes of section 408 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174 ).\n##### (c) Applicability\nThis section shall apply to funds appropriated on or after the date of enactment of this Act.\n#### 4. Repair and rebuilding\n##### (a) Housing assistance\nSection 408(b)(1) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(b)(1) ) is amended\u2014\n**(1)**\nby striking rendered uninhabitable and inserting damaged by a major disaster ; and\n**(2)**\nby striking uninhabitable, as a result of damage caused by a major disaster and inserting damaged by a major disaster .\n##### (b) Types of housing assistance\nSection 408(c)(4) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174 ) is amended by striking in cases in which and all that follows through the end of the paragraph and inserting if the President determines such assistance is a cost effective alternative to other housing solutions, including the costs associated with temporary housing provided under this section. .\n##### (c) Provision of grants as pilot program\nSection 408(f)(3)(J) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(f)(3)(J) ) is amended\u2014\n**(1)**\nin clause (ii) by striking Not later than 2 years after the date of enactment of this paragraph, the Administrator and inserting The Administrator ; and\n**(2)**\nin clause (iii)\u2014\n**(A)**\nby striking 2 years after the date of enactment of this paragraph or ; and\n**(B)**\nby striking , whichever occurs sooner .\n##### (d) Applicability\nThis section and the amendments made by this section shall only apply to\u2014\n**(1)**\napplications received on or after the date of enactment of this Act; and\n**(2)**\namounts appropriated on or after the date of enactment of this Act.\n#### 5. Determination of budgetary effects\nThe budgetary effects of this Act, for the purpose of complying with the Statutory Pay-As-You-Go Act of 2010, shall be determined by reference to the latest statement titled Budgetary Effects of PAYGO Legislation for this Act, submitted for printing in the Congressional Record by the Chairman of the House Budget Committee, provided that such statement has been submitted prior to the vote on passage.",
      "versionDate": "2025-01-15",
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
        "name": "Emergency Management",
        "updateDate": "2025-02-18T20:51:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr426",
          "measure-number": "426",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-06-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr426v00",
            "update-date": "2025-06-23"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Housing Survivors of Major Disasters Act</strong></p><p>This bill expands eligibility for disaster housing assistance under the Federal Emergency Management Agency (FEMA) Individuals and Households Program (IHP) with respect to property damage, availability of housing resources, and constructive (i.e., implied) ownership. \u00a0</p><p>Specifically, the bill lowers the level of damage required to be eligible for IHP housing assistance, so the residence must be damaged by a major disaster instead of rendered uninhabitable.</p><p>Also, under current law, FEMA is authorized to provide IHP assistance for permanent housing construction where (1) no alternative housing resources are available; and (2) other types of temporary housing assistance are unavailable, infeasible, or not cost-effective. The bill authorizes IHP permanent housing construction where FEMA determines such assistance is a cost-effective alternative to other housing solutions, such as providing for temporary housing costs.</p><p>Additionally, the bill requires\u00a0FEMA to consider an individual's or household\u2019s claim of constructive ownership, where evidence supports such ownership is more likely than not, when determining eligibility for IHP financial assistance for home repair or replacement for a residence without documented ownership rights. FEMA must consider all evidence provided (e.g., deeds, tax receipts, insurance documents) when determining whether constructive ownership more likely than not exists. If FEMA determines the evidence is insufficient, FEMA may require a signed declarative statement describing the constructive ownership.</p>"
        },
        "title": "Housing Survivors of Major Disasters Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr426.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Housing Survivors of Major Disasters Act</strong></p><p>This bill expands eligibility for disaster housing assistance under the Federal Emergency Management Agency (FEMA) Individuals and Households Program (IHP) with respect to property damage, availability of housing resources, and constructive (i.e., implied) ownership. \u00a0</p><p>Specifically, the bill lowers the level of damage required to be eligible for IHP housing assistance, so the residence must be damaged by a major disaster instead of rendered uninhabitable.</p><p>Also, under current law, FEMA is authorized to provide IHP assistance for permanent housing construction where (1) no alternative housing resources are available; and (2) other types of temporary housing assistance are unavailable, infeasible, or not cost-effective. The bill authorizes IHP permanent housing construction where FEMA determines such assistance is a cost-effective alternative to other housing solutions, such as providing for temporary housing costs.</p><p>Additionally, the bill requires\u00a0FEMA to consider an individual's or household\u2019s claim of constructive ownership, where evidence supports such ownership is more likely than not, when determining eligibility for IHP financial assistance for home repair or replacement for a residence without documented ownership rights. FEMA must consider all evidence provided (e.g., deeds, tax receipts, insurance documents) when determining whether constructive ownership more likely than not exists. If FEMA determines the evidence is insufficient, FEMA may require a signed declarative statement describing the constructive ownership.</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119hr426"
    },
    "title": "Housing Survivors of Major Disasters Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Housing Survivors of Major Disasters Act</strong></p><p>This bill expands eligibility for disaster housing assistance under the Federal Emergency Management Agency (FEMA) Individuals and Households Program (IHP) with respect to property damage, availability of housing resources, and constructive (i.e., implied) ownership. \u00a0</p><p>Specifically, the bill lowers the level of damage required to be eligible for IHP housing assistance, so the residence must be damaged by a major disaster instead of rendered uninhabitable.</p><p>Also, under current law, FEMA is authorized to provide IHP assistance for permanent housing construction where (1) no alternative housing resources are available; and (2) other types of temporary housing assistance are unavailable, infeasible, or not cost-effective. The bill authorizes IHP permanent housing construction where FEMA determines such assistance is a cost-effective alternative to other housing solutions, such as providing for temporary housing costs.</p><p>Additionally, the bill requires\u00a0FEMA to consider an individual's or household\u2019s claim of constructive ownership, where evidence supports such ownership is more likely than not, when determining eligibility for IHP financial assistance for home repair or replacement for a residence without documented ownership rights. FEMA must consider all evidence provided (e.g., deeds, tax receipts, insurance documents) when determining whether constructive ownership more likely than not exists. If FEMA determines the evidence is insufficient, FEMA may require a signed declarative statement describing the constructive ownership.</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119hr426"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr426ih.xml"
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
      "title": "Housing Survivors of Major Disasters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Survivors of Major Disasters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make available necessary disaster assistance for families affected by major disasters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T02:48:19Z"
    }
  ]
}
```
