# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6543?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6543
- Title: Health Care Worker and First Responder Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 6543
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-04-02T19:46:44Z
- Update date including text: 2026-04-02T19:46:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6543",
    "number": "6543",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Health Care Worker and First Responder Fairness Act",
    "type": "HR",
    "updateDate": "2026-04-02T19:46:44Z",
    "updateDateIncludingText": "2026-04-02T19:46:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:00:35Z",
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
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MD"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6543ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6543\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Thompson of Pennsylvania (for himself and Mrs. McClain Delaney ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide for the exemption of certain earnings from the retirement earnings test, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Care Worker and First Responder Fairness Act .\n#### 2. Exemption of certain earnings from retirement earnings test\n##### (a) In general\nFor purposes of subsection (b) of section 203 of the Social Security Act ( 42 U.S.C. 403(b) ), wages paid during the period beginning on January 31, 2020, and ending on May 11, 2023, to an individual who attests to and provides evidence of being employed as a health care professional or first responder during such period shall not be included in the determination of the individual\u2019s excess earnings under subsection (f)(3) of such section for any taxable year.\n##### (b) Guidance\nNot later than 30 days after the date of the enactment of this Act, the Commissioner of Social Security shall issue guidance providing for appropriate procedures for the implementation of subsection (a).\n#### 3. Future pandemic preparedness\n##### (a) In general\nFor purposes of subsection (b) of section 203 of the Social Security Act ( 42 U.S.C. 403(b) ), wages paid to an eligible individual during any public health emergency declared by the Secretary of Health and Human Services under section 319(a) of the Public Health Service Act ( 42 U.S.C. 247d(a) ) shall not be included in the determination of the individual\u2019s excess earnings under subsection (f)(3) of such section for any taxable year.\n##### (b) Issuance of waivers\nDuring a public health emergency declared by the Secretary under section 319(a) of the Public Health Service Act ( 42 U.S.C. 247d(a) ) in which the Secretary has determined that, wholly or partially as a result of the public health emergency, there is a shortage of healthcare workers, the Commissioner of Social Security may issue a waiver to an individual who attests to and provides evidence of being employed as a health care professional or first responder during such public health emergency.\n##### (c) Report\nThe Commissioner shall annually submit a report to Congress describing each waiver that has been issued under this section during the previous year.\n##### (d) Eligible individual defined\nFor purposes of this section, the term eligible individual means an individual to whom the Commissioner has issued a waiver in accordance with subsection (b).\n#### 4. Definitions\nIn this Act:\n**(1) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(2) Health care professional**\nThe term health care professional has the meaning given such term in section 225(d)(1) of the Public Health Service Act ( 42 U.S.C. 234(d)(1) ).\n**(3) First responder**\nThe term first responder has the meaning given such term in section 3025(1) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10705(1) ).\n**(4) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.",
      "versionDate": "2025-12-09",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-07T17:22:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-09",
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
          "measure-id": "id119hr6543",
          "measure-number": "6543",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-09",
          "originChamber": "HOUSE",
          "update-date": "2026-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6543v00",
            "update-date": "2026-04-02"
          },
          "action-date": "2025-12-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Health Care Worker and First Responder Fairness Act</strong></p><p>This bill exempts from the Social Security Retirement Earnings Test (RET) wages earned through work as a health care professional or first responder during the COVID-19 pandemic. Under the RET, benefits are reduced for beneficiaries who are younger than full retirement age if they earn wages in excess of a specified annual limit.\u00a0</p><p>Further, the Social Security Administration may issue waivers to individuals employed as health care professionals or first responders during a declared public health emergency in which there is a shortage of health care workers. Wages earned by individuals granted waivers during a public health emergency are exempt from the RET.\u00a0</p>"
        },
        "title": "Health Care Worker and First Responder Fairness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6543.xml",
    "summary": {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Health Care Worker and First Responder Fairness Act</strong></p><p>This bill exempts from the Social Security Retirement Earnings Test (RET) wages earned through work as a health care professional or first responder during the COVID-19 pandemic. Under the RET, benefits are reduced for beneficiaries who are younger than full retirement age if they earn wages in excess of a specified annual limit.\u00a0</p><p>Further, the Social Security Administration may issue waivers to individuals employed as health care professionals or first responders during a declared public health emergency in which there is a shortage of health care workers. Wages earned by individuals granted waivers during a public health emergency are exempt from the RET.\u00a0</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hr6543"
    },
    "title": "Health Care Worker and First Responder Fairness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Health Care Worker and First Responder Fairness Act</strong></p><p>This bill exempts from the Social Security Retirement Earnings Test (RET) wages earned through work as a health care professional or first responder during the COVID-19 pandemic. Under the RET, benefits are reduced for beneficiaries who are younger than full retirement age if they earn wages in excess of a specified annual limit.\u00a0</p><p>Further, the Social Security Administration may issue waivers to individuals employed as health care professionals or first responders during a declared public health emergency in which there is a shortage of health care workers. Wages earned by individuals granted waivers during a public health emergency are exempt from the RET.\u00a0</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hr6543"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6543ih.xml"
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
      "title": "Health Care Worker and First Responder Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Care Worker and First Responder Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the exemption of certain earnings from the retirement earnings test, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:23Z"
    }
  ]
}
```
