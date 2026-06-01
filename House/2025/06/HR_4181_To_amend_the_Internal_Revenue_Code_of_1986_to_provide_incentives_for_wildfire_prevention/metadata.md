# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4181?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4181
- Title: WILTR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4181
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2025-10-04T08:05:56Z
- Update date including text: 2025-10-04T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4181",
    "number": "4181",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "WILTR Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:56Z",
    "updateDateIncludingText": "2025-10-04T08:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:08:05Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AZ"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "OH"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "TX"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4181ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4181\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Issa (for himself, Mr. Baumgartner , Mr. Gosar , Mr. Newhouse , and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide incentives for wildfire prevention.\n#### 1. Short title\nThis Act may be cited as the Wildfire Infrastructure and Landowner Tax Relief Act of 2025 or the WILTR Act of 2025 .\n#### 2. Exclusion of gross income related to hazardous fuel reduction activities\n##### (a) In general\nSection 139 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(i) Hazardous fuel reduction activities on and improvements to real property (1) In general Gross income shall not include any grant or award received by a taxpayer or services provided to the taxpayer for the purpose of conducting hazardous fuel reduction activities on or hazardous fuel reduction improvements to the real property of such taxpayer. (2) Definitions For purposes of this section\u2014 (A) Hazardous fuel reduction activity The term hazardous fuel reduction activity means an activity the purpose of which is wildfire prevention through\u2014 (i) the installation of\u2014 (I) a natural or manmade change in fuel characteristics that affects fire behavior such that a fire can be more readily controlled (commonly known as a fuel break) , or (II) a natural or constructed barrier used to stop or check a fire or to provide a control line from which to work to stop or check a fire (commonly known as a firebreak ), or (ii) reduction of hazardous fuels, including\u2014 (I) prescribed fire, (II) wildland fire use, and (III) the use of mechanical methods such as crushing, tractor and hand piling, thinning, pruning, cutting, or otherwise removing hazardous fuels. (B) Hazardous fuel reduction improvement The term hazardous fuel reduction improvement means additions or alterations to real property the purpose of which is to enable firefighting preparation, training, access, or fire suppression or emergency evacuation relating to fire, including\u2014 (i) the installation of firefighting equipment or infrastructure, (ii) the maintenance, expansion, or alteration of trails or roads for the purposes of firefighting access or fire-related evacuation, and (iii) the facilitation of firefighter training on such real property. (C) Hazardous fuel The term hazardous fuel means any vegetative material that is susceptible to burning, including\u2014 (i) trees, (ii) grasses, (iii) shrubs, (iv) sagebrush, (v) chaparral, and (vi) any dead vegetative material on or near the ground. .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts received after the date of the enactment of this Act.\n#### 3. Treatment of expenditures in connection with hazardous fuel reduction activities or improvements\n##### (a) In general\nPart VI of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 199A the following new section:\n199B. Deduction for hazardous fuel reduction activities or improvements (a) In general There shall be allowed as a deduction an amount equal to the amounts paid or incurred by the taxpayer for qualified hazardous fuel reduction activities during the taxable year. (b) Qualified hazardous fuel reduction activities For purposes of this section, the term qualified hazardous fuel reduction activities means improvements to the real property of the taxpayer which\u2014 (1) is a hazardous fuel reduction activity or hazardous fuel reduction improvement described in section 139(i)(2), and (2) a State, local, Tribal, or Federal fire management agency certifies will reduce hazardous fuels or enable firefighting preparation, training, access, or fire suppression or emergency evacuation relating to fire. (c) Denial of double benefit No deduction shall be allowed under subsection (a) with respect to any expenditure to the extent that an amount is excludable under section 139(i) with respect to such expenditure. .\n##### (b) Deduction taken into account in determining adjusted gross income\nSection 62(a) of such Code is amended by inserting after paragraph (21) the following new paragraph:\n(22) Expenditures in connection with qualified hazardous fuel reduction activities The deduction allowed by section 199B. .\n##### (c) Conforming amendments\n**(1)**\nSection 263(a)(1) of such Code is amended by striking or at the end of subparagraph (J), by striking the period at the end of subparagraph (K) and inserting , or , and by adding at the end the following new subparagraph:\n(L) expenditures for which a deduction is allowed under section 200. .\n**(2)**\nThe table of sections for part VI of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 199A the following new item:\nSec. 199B. Deduction for hazardous fuel reduction activities or improvements. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act.",
      "versionDate": "2025-06-26",
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
        "updateDate": "2025-07-17T19:05:48Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4181ih.xml"
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
      "title": "WILTR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WILTR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Infrastructure and Landowner Tax Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide incentives for wildfire prevention.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T04:18:27Z"
    }
  ]
}
```
