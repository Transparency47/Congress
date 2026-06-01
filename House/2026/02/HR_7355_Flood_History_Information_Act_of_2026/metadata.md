# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7355?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7355
- Title: Flood History Information Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7355
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-20T16:58:25Z
- Update date including text: 2026-02-20T16:58:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7355",
    "number": "7355",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000631",
        "district": "4",
        "firstName": "Madeleine",
        "fullName": "Rep. Dean, Madeleine [D-PA-4]",
        "lastName": "Dean",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Flood History Information Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-20T16:58:25Z",
    "updateDateIncludingText": "2026-02-20T16:58:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:01:10Z",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7355ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7355\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. Dean of Pennsylvania (for herself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide for the disclosure and sharing of certain policy and claims information under the National Flood Insurance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flood History Information Act of 2026 .\n#### 2. Data exchange program\nSection 1313 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4020 ) is amended\u2014\n**(1)**\nby striking The Administrator shall and inserting the following:\n(a) Availability of flood insurance information The Administrator shall ; and\n**(2)**\nby adding at the end the following new subsections:\n(b) Data exchange program (1) In general The Administrator shall disclose policy and claims information described in paragraph (2) to an insurance company, as such term is defined in subsection (f), if such insurance company has entered into a data sharing agreement with the Administrator pursuant to paragraph (3). (2) Data eligible for sharing The Administrator shall disclose the following claims and policy information, obtained in connection with a flood insurance policy made available under this title or through a data sharing agreement executed pursuant to paragraph (3), pursuant to paragraph (1): (A) The location of the insured property, by address and latitude and longitude. (B) Amount of coverage in force. (C) Dates of loss. (D) The amount paid on claims. (E) Any other claims and policy information the Administrator determines necessary and appropriate. (3) Data sharing agreement A data sharing agreement entered into pursuant to paragraph (1) shall include\u2014 (A) the terms and conditions under which insurance companies may use, share, store, and account for the data, which shall at minimum include provisions ensuring that\u2014 (i) the insurance company may only use information provided under the agreement for the purposes of underwriting, establishing premium rates, and adjusting claims; and (ii) the insurance company may not use the information provided as part of the agreement for marketing purposes; (B) an agreement by the insurance company to provide to the Administrator the insurance company\u2019s policy and claims data in a form prescribed by the Administrator; and (C) any other terms and conditions the Administrator determines are necessary and appropriate. (c) Access to flood insurance information Upon the request of a purchaser, lessee, or current owner of a property, the Administrator shall provide to the purchaser, lessee, or current owner of the property information pertaining to the property the purchaser or lessee is under contract to buy or lease, respectively, or the current owner\u2019s property, as follows: (1) The number and dollar value of claims filed for the property, and factors related to the cause of loss, over the life of the property, as known to the Administrator, including claims made under\u2014 (A) a flood insurance policy made available under this Act; and (B) a private flood insurance policy. (2) Information on whether the property owner may be required to purchase flood insurance coverage due to previous receipt of Federal disaster assistance subject to the mandatory purchase requirement under section 102 of the Flood Disaster Protection Act of 1973. (3) Such other available information about the property as determined by the Administrator to accurately and adequately characterize the true flood risk to the property. (d) Privacy protection Disclosure of information contained within a system of records (as such term is defined in section 552a(a)(5) of title 5, United States Code) as authorized in subsections (b) and (c) of this section shall be considered a routine use for the purposes of section 552a(3) of title 5, United States Code. (e) Fee (1) In general To carry out subsection (b), the Administrator may charge a fee to participating insurance companies under subsection (b). The Administrator shall not charge a fee to the current owner requesting flood insurance information under subsection (c). (2) Deposit The Administrator shall deposit the fee collected under this subsection into the National Flood Insurance Fund established under section 1310. (f) Definition For the purposes of this section the following definitions shall apply: (1) Insurance company The term insurance company means an insurance company that meets the requirements of subparagraph (A) of section 102(b)(7) of the Flood Disaster Protection Act of 1973 ( 42 U.S.C. 4012a(b)(7)(A) ). (2) Lessee The term lessee means a person who enters into an agreement to lease, rent, or sublease a property. (3) Purchaser The term purchaser means a person or entity that enters into an agreement to purchase an interest in a property. .",
      "versionDate": "2026-02-04",
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
        "updateDate": "2026-02-20T16:58:25Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7355ih.xml"
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
      "title": "Flood History Information Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Flood History Information Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the disclosure and sharing of certain policy and claims information under the National Flood Insurance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T04:03:36Z"
    }
  ]
}
```
