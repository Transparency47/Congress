# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/492
- Title: Directing the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1.
- Congress: 119
- Bill type: HRES
- Bill number: 492
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2025-10-09T03:26:22Z
- Update date including text: 2025-10-09T03:26:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Submitted in House
- 2025-06-10 - IntroReferral: Submitted in House
- 2025-06-11 16:51:25 - Floor: Pursuant to the provisions of H. Res. 499, H. Res. 492 is considered passed House.
- 2025-06-11 16:51:25 - Floor: Pursuant to the provisions of H. Res. 499, H. Res. 492 is considered passed House. (consideration: CR H2647; text: CR H2647)
- Latest action: 2025-06-10: Submitted in House

## Actions

- 2025-06-10 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Submitted in House
- 2025-06-10 - IntroReferral: Submitted in House
- 2025-06-11 16:51:25 - Floor: Pursuant to the provisions of H. Res. 499, H. Res. 492 is considered passed House.
- 2025-06-11 16:51:25 - Floor: Pursuant to the provisions of H. Res. 499, H. Res. 492 is considered passed House. (consideration: CR H2647; text: CR H2647)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/492",
    "number": "492",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Directing the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1.",
    "type": "HRES",
    "updateDate": "2025-10-09T03:26:22Z",
    "updateDateIncludingText": "2025-10-09T03:26:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1B000",
      "actionDate": "2025-06-11",
      "actionTime": "16:51:25",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Pursuant to the provisions of H. Res. 499, H. Res. 492 is considered passed House. (consideration: CR H2647; text: CR H2647)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-06-11",
      "actionTime": "16:51:25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Pursuant to the provisions of H. Res. 499, H. Res. 492 is considered passed House.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
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
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-10T14:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-10T14:06:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres492ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 492\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Arrington submitted the following resolution; which was referred to the Committee on the Budget , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nDirecting the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1.\nThat the Clerk of the House of Representatives shall, in the engrossment of the bill H.R. 1, make the following corrections:\n**(1)**\nIn section 10004(a), strike (1) Standard Utility Allowance.\u2014 Section and insert Section .\n**(2)**\nIn section 10004(a), strike paragraph (2).\n**(3)**\nIn section 10106, strike subsection (a).\n**(4)**\nIn section 10106, strike (b) Bioenergy program for advanced biofuels.\u2014 Section and insert Section .\n**(5)**\nIn paragraph (17) of section 20005, strike and intelligence .\n**(6)**\nIn section 20005, strike paragraph (21).\n**(7)**\nIn section 20008(a), strike paragraph (8).\n**(8)**\nIn paragraph (16) of section 20009, strike intelligence, surveillance, and insert surveillance .\n**(9)**\nIn paragraph (17) of section 20009, strike intelligence, surveillance, and insert surveillance .\n**(10)**\nStrike section 20012.\n**(11)**\nIn section 44124(a)(1), in the matter proposed to be added as new paragraph (6)(A)(i)(III) of section 1927(e) of the Social Security Act ( 42 U.S.C. 1396r\u20138(e) ), strike (or any successor regulation) .\n**(12)**\nIn section 44124(a)(1), in the matter proposed to be added as new paragraph (6)(A)(i)(III) of section 1927(e) of the Social Security Act ( 42 U.S.C. 1396r\u20138(e) ), strike , or any successor regulation .\n**(13)**\nIn section 44133, strike (or a successor regulation) each place it appears.\n**(14)**\nIn section 44201, strike (or any successor regulation) each place it appears.\n**(15)**\nIn section 44201, strike (or a successor regulation) each place it appears.\n**(16)**\nIn section 44302(a), in the matter proposed to be added as new paragraph (10)(B)(i)(III)(bb) of section 1902(kk) of the Social Security Act ( 42 U.S.C. 1396a(kk) ), strike (or any successor regulation) .\n**(17)**\nIn section 44305(a)(1), in the matter proposed to be added as new subsection (h)(1)(B)(i) of section 1860D\u201312 of the Social Security Act ( 42 U.S.C. 1395w\u2013112 ), strike or a successor regulation each place it appears.\n**(18)**\nIn section 80101(c)(1), in the matter proposed to be added as new paragraph (2) of section 17(a) of the Mineral Leasing Act ( 30 U.S.C. 226 ), strike such paragraph and insert the following:\n(2) Land use plans terms and conditions A lease issued by the Secretary under this section\u2014 (A) shall include any terms and conditions of the land use plan that apply to the area of the lease; and (B) shall not require any stipulations or mitigation requirements not included in such land use plan. .\n**(19)**\nStrike section 80131.\n**(20)**\nStrike section 112205.",
      "versionDate": "2025-06-10",
      "versionType": "IH"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres492eh.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 492\nIn the House of Representatives, U. S.,\nJune 11, 2025\nRESOLUTION\nDirecting the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1.\nThat the Clerk of the House of Representatives shall, in the engrossment of the bill H.R. 1, make the following corrections:\n**(1)**\nIn section 10004(a), strike (1) Standard Utility Allowance.\u2014 Section and insert Section .\n**(2)**\nIn section 10004(a), strike paragraph (2).\n**(3)**\nIn section 10106, strike subsection (a).\n**(4)**\nIn section 10106, strike (b) Bioenergy program for advanced biofuels.\u2014 Section and insert Section .\n**(5)**\nIn paragraph (17) of section 20005, strike and intelligence .\n**(6)**\nIn section 20005, strike paragraph (21).\n**(7)**\nIn section 20008(a), strike paragraph (8).\n**(8)**\nIn paragraph (16) of section 20009, strike intelligence, surveillance, and insert surveillance .\n**(9)**\nIn paragraph (17) of section 20009, strike intelligence, surveillance, and insert surveillance .\n**(10)**\nStrike section 20012.\n**(11)**\nIn section 44124(a)(1), in the matter proposed to be added as new paragraph (6)(A)(i)(III) of section 1927(e) of the Social Security Act ( 42 U.S.C. 1396r\u20138(e) ), strike (or any successor regulation) .\n**(12)**\nIn section 44124(a)(1), in the matter proposed to be added as new paragraph (6)(A)(i)(III) of section 1927(e) of the Social Security Act ( 42 U.S.C. 1396r\u20138(e) ), strike , or any successor regulation .\n**(13)**\nIn section 44133, strike (or a successor regulation) each place it appears.\n**(14)**\nIn section 44201, strike (or any successor regulation) each place it appears.\n**(15)**\nIn section 44201, strike (or a successor regulation) each place it appears.\n**(16)**\nIn section 44302(a), in the matter proposed to be added as new paragraph (10)(B)(i)(III)(bb) of section 1902(kk) of the Social Security Act ( 42 U.S.C. 1396a(kk) ), strike (or any successor regulation) .\n**(17)**\nIn section 44305(a)(1), in the matter proposed to be added as new subsection (h)(1)(B)(i) of section 1860D\u201312 of the Social Security Act ( 42 U.S.C. 1395w\u2013112 ), strike or a successor regulation each place it appears.\n**(18)**\nIn section 80101(c)(1), in the matter proposed to be added as new paragraph (2) of section 17(a) of the Mineral Leasing Act ( 30 U.S.C. 226 ), strike such paragraph and insert the following:\n(2) Land use plans terms and conditions A lease issued by the Secretary under this section\u2014 (A) shall include any terms and conditions of the land use plan that apply to the area of the lease; and (B) shall not require any stipulations or mitigation requirements not included in such land use plan. .\n**(19)**\nStrike section 80131.\n**(20)**\nStrike section 112205.",
      "versionDate": "2025-06-11",
      "versionType": "EH"
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
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "House",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-11",
        "actionTime": "16:51:08",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "499",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "House",
          "type": "Procedurally related"
        }
      },
      "title": "Providing for consideration of the bill (H.R. 4) to rescind certain budget authority proposed to be rescinded in special messages transmitted to the Congress by the President on June 3, 2025, in accordance with section 1012(a) of the Congressional Budget and Impoundment Control Act of 1974, and for other purposes.",
      "type": "HRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-26T17:04:54Z"
          },
          {
            "name": "Agricultural marketing and promotion",
            "updateDate": "2025-06-26T17:04:01Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-06-26T17:04:47Z"
          },
          {
            "name": "Energy assistance for the poor and aged",
            "updateDate": "2025-06-26T17:03:50Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-06-24T17:36:56Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-06-26T17:04:38Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-06-26T17:04:08Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-06-26T17:04:32Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-06-24T17:37:03Z"
          },
          {
            "name": "Military procurement, research, weapons development",
            "updateDate": "2025-06-26T17:04:15Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-06-26T17:04:27Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2025-06-26T17:04:59Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-06-26T17:04:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-06-16T15:28:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-10",
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
          "measure-id": "id119hres492",
          "measure-number": "492",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-10",
          "originChamber": "HOUSE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres492v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-06-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution directs the Clerk of the House of Representatives to make several corrections in the engrossment of H.R. 1 (One Big Beautiful Bill Act).\u00a0</p><p>Specifically, the corrections strike provisions from the bill that\u00a0</p><ul><li>make a conforming amendment to the Low-Income Home Energy Assistance Act;</li><li>reauthorize,\u00a0and extend funding for, the Department of Agriculture's biobased markets program (i.e., BioPreferred Program) through FY2031;</li><li>provide funding to the Department of Defense (DOD) for various intelligence-related activities and equipment, including enhancements to military intelligence programs;</li><li>provide funding to DOD for exportable low-cost cruise missiles;</li><li>provide funding for DOD to convert Ohio-class submarine tubes to accept additional missiles;</li><li>specify that revisions to a land use plan may not prevent or delay the Department of the Interior from leasing certain federal land for oil and natural gas development;\u00a0</li><li>nullify the Bureau of Land Management\u2019s Public Land Order No. 7917 for Withdrawal of Federal Lands; Cook, Lake, and Saint Louis Counties, MN that was published on January 31, 2023;</li><li>reinstate certain\u00a0hardrock mineral leases in the Superior National Forest in Minnesota;\u00a0</li><li>increase the penalty for aiding and abetting the understatement of tax liability with respect to the employee retention tax credit (ERTC) by a COVID-ERTC promoter and make other changes related to the\u00a0ERTC; and</li><li>specify that provisions in the bill\u00a0regarding certain Department of Health and Human Services regulations also apply to successor regulations.</li></ul>"
        },
        "title": "Directing the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres492.xml",
    "summary": {
      "actionDate": "2025-06-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution directs the Clerk of the House of Representatives to make several corrections in the engrossment of H.R. 1 (One Big Beautiful Bill Act).\u00a0</p><p>Specifically, the corrections strike provisions from the bill that\u00a0</p><ul><li>make a conforming amendment to the Low-Income Home Energy Assistance Act;</li><li>reauthorize,\u00a0and extend funding for, the Department of Agriculture's biobased markets program (i.e., BioPreferred Program) through FY2031;</li><li>provide funding to the Department of Defense (DOD) for various intelligence-related activities and equipment, including enhancements to military intelligence programs;</li><li>provide funding to DOD for exportable low-cost cruise missiles;</li><li>provide funding for DOD to convert Ohio-class submarine tubes to accept additional missiles;</li><li>specify that revisions to a land use plan may not prevent or delay the Department of the Interior from leasing certain federal land for oil and natural gas development;\u00a0</li><li>nullify the Bureau of Land Management\u2019s Public Land Order No. 7917 for Withdrawal of Federal Lands; Cook, Lake, and Saint Louis Counties, MN that was published on January 31, 2023;</li><li>reinstate certain\u00a0hardrock mineral leases in the Superior National Forest in Minnesota;\u00a0</li><li>increase the penalty for aiding and abetting the understatement of tax liability with respect to the employee retention tax credit (ERTC) by a COVID-ERTC promoter and make other changes related to the\u00a0ERTC; and</li><li>specify that provisions in the bill\u00a0regarding certain Department of Health and Human Services regulations also apply to successor regulations.</li></ul>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hres492"
    },
    "title": "Directing the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1."
  },
  "summaries": [
    {
      "actionDate": "2025-06-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution directs the Clerk of the House of Representatives to make several corrections in the engrossment of H.R. 1 (One Big Beautiful Bill Act).\u00a0</p><p>Specifically, the corrections strike provisions from the bill that\u00a0</p><ul><li>make a conforming amendment to the Low-Income Home Energy Assistance Act;</li><li>reauthorize,\u00a0and extend funding for, the Department of Agriculture's biobased markets program (i.e., BioPreferred Program) through FY2031;</li><li>provide funding to the Department of Defense (DOD) for various intelligence-related activities and equipment, including enhancements to military intelligence programs;</li><li>provide funding to DOD for exportable low-cost cruise missiles;</li><li>provide funding for DOD to convert Ohio-class submarine tubes to accept additional missiles;</li><li>specify that revisions to a land use plan may not prevent or delay the Department of the Interior from leasing certain federal land for oil and natural gas development;\u00a0</li><li>nullify the Bureau of Land Management\u2019s Public Land Order No. 7917 for Withdrawal of Federal Lands; Cook, Lake, and Saint Louis Counties, MN that was published on January 31, 2023;</li><li>reinstate certain\u00a0hardrock mineral leases in the Superior National Forest in Minnesota;\u00a0</li><li>increase the penalty for aiding and abetting the understatement of tax liability with respect to the employee retention tax credit (ERTC) by a COVID-ERTC promoter and make other changes related to the\u00a0ERTC; and</li><li>specify that provisions in the bill\u00a0regarding certain Department of Health and Human Services regulations also apply to successor regulations.</li></ul>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hres492"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres492ih.xml"
        }
      ],
      "type": "IH"
    },
    {
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres492eh.xml"
        }
      ],
      "type": "EH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Directing the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T08:18:21Z"
    },
    {
      "title": "Directing the Clerk of the House of Representatives to make a correction in the engrossment of H.R. 1.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T08:06:26Z"
    }
  ]
}
```
