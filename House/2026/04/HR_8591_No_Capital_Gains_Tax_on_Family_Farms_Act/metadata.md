# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8591?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8591
- Title: No Capital Gains Tax on Family Farms Act
- Congress: 119
- Bill type: HR
- Bill number: 8591
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-13T08:06:01Z
- Update date including text: 2026-05-13T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8591",
    "number": "8591",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "No Capital Gains Tax on Family Farms Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:01Z",
    "updateDateIncludingText": "2026-05-13T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:01:00Z",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "WA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "OH"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "CO"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "SC"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NC"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "MO"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "GA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "ND"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8591ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8591\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Massie (for himself, Ms. Perez , Mr. Roy , Mr. Davidson , Mr. Burchett , Ms. Boebert , Ms. Mace , Mr. Edwards , Mr. Burlison , Mr. Collins , and Ms. Fedorchak ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an exclusion from gross income of gain from the sale of qualified farm property to qualified family members.\n#### 1. Short title\nThis Act may be cited as the No Capital Gains Tax on Family Farms Act .\n#### 2. Exclusion from gross income of gain from sale of qualified farm property to qualified family members\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 121 the following new section:\n121A. Exclusion of gain from sale of qualified farm property to qualified family members (a) Exclusion Gross income shall not include gain from the sale or exchange of qualified farm property to a qualified family member of the taxpayer. (b) Definitions For purposes of this section\u2014 (1) Qualified farm property The term qualified farm property means any interest in real property located in the United States if, during periods aggregating 2 years or more during the 8-year period ending on the date of the sale or exchange of such real property, such real property was owned and used as a farm for farming purposes (within the meaning of section 2032A(e)) by the taxpayer. (2) Qualified family member The term qualified family member means, with respect to any taxpayer\u2014 (A) the spouse of such taxpayer, (B) a lineal descendant of such taxpayer, of such taxpayer\u2019s spouse, of a parent of such taxpayer, or of a parent of such taxpayer\u2019s spouse, or (C) the spouse of any lineal descendant described in subparagraph (B). For purposes of the preceding sentence, a legally adopted child of an individual shall be treated as the child of such individual by blood. (c) Special rules (1) Basis of qualified farm property For purposes of this section\u2014 (A) In general The basis of qualified farm property in the hands of a qualified family member following a sale or exchange described in subsection (a) shall be the adjusted basis of such qualified farm property in the hands of the taxpayer immediately before such sale or exchange. (B) Increased basis following 10-year holding period If, following a sale or exchange described in subsection (a), the qualified farm property is not sold, exchanged, or otherwise disposed of for the 10-year period beginning on the date of such sale or exchange, the basis of such qualified farm property in the hands of the qualified family member (as of the first day following such 10-year period) shall be increased by an amount equal to the excess (if any) of\u2014 (i) the fair market value of such qualified farm property (as of the date of such sale or exchange), over (ii) the basis of such qualified farm property in the hands of such qualified family member (as otherwise determined under subparagraph (A)). (2) Election to have section not apply Rules similar to the rules of section 121(f) shall apply for purposes of this section. (d) Regulations The Secretary shall prescribe such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including with respect to the application of subsection (c)(1)(B) in cases other than where the entire interest in qualified farm property is not sold, exchanged, or otherwise disposed of for the applicable 10-year period. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 121 the following new item:\nSec. 121A. Exclusion of gain from sale of qualified farm property to qualified family members. .\n##### (c) Effective date\nThe amendments made by this section shall apply to sales or exchanges after the date of the enactment of this Act.",
      "versionDate": "2026-04-30",
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
        "updateDate": "2026-05-07T02:42:59Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8591ih.xml"
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
      "title": "No Capital Gains Tax on Family Farms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-02T03:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Capital Gains Tax on Family Farms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-02T03:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide an exclusion from gross income of gain from the sale of qualified farm property to qualified family members.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-02T03:33:33Z"
    }
  ]
}
```
