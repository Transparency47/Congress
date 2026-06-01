# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6594?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6594
- Title: Medical Device Recall Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6594
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-07T17:51:07Z
- Update date including text: 2026-01-07T17:51:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6594",
    "number": "6594",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Medical Device Recall Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T17:51:07Z",
    "updateDateIncludingText": "2026-01-07T17:51:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:06:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6594ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6594\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Ms. Schakowsky (for herself and Mr. Carson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve medical device recall notifications by amending the Federal Food, Drug, and Cosmetic Act to establish an electronic format for device recall notifications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Device Recall Improvement Act of 2025 .\n#### 2. Regulation of medical device recalls\nChapter V of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 351 et seq. ), is amended by inserting after section 518A of such Act the following:\n518B. Electronic notification format for device recalls (a) Electronic notification format for device recalls (1) In general Not later than 2 years after the date of enactment of the Medical Device Recall Improvement Act of 2025 , the Secretary shall publish a form and manner for notifications of a recall. (2) Content The form and manner prescribed by the Secretary under paragraph (1) shall\u2014 (A) be electronic; (B) include mandatory data elements, including\u2014 (i) the name of the manufacturer or importer; (ii) the contact information and address of the manufacturer or importer; (iii) the specific reason for the correction or removal from the market of the device; (iv) the specific device of the manufacturer or importer subject to such recall; (v) the unique device identifier of the device, including, as applicable, the device identifier and any production identifier; (vi) information for device user facilities and health professionals with regard to the device and such recall; and (vii) information for patients with regard to the device and such recall, including\u2014 (I) the risk presented by the device; and (II) any action that may be taken by, or on behalf of, such patients to eliminate or reduce such risk; and (C) include optional data elements as the Secretary determines to be appropriate. (b) Notifications (1) Notifications to the Secretary (A) In general Beginning 180 days after the Secretary establishes the form and manner for recall notifications under subsection (a), a manufacturer or importer of a device shall submit notifications required under section 519(g) to the Secretary through the electronic notification format established under subsection (a). (B) Review requirement (i) Initial review Not later than 2 business days after receipt of a notification described in subparagraph (A), the Secretary shall conduct an initial review of such notification. (ii) Response of the Secretary Not later than 3 business days after the completion of such review, the Secretary shall inform the manufacturer or importer of the information the Secretary determines, through the initial review under clause (i), should be shared with device user facilities and health professionals. (2) Notifications to device user facilities and health professionals (A) Initial notifications A manufacturer or importer shall submit notifications to device user facilities and health professionals through the electronic notification format established under subsection (a) after an initial review by the Secretary is completed under paragraph (1)(B)(i). (B) Subsequent notifications A manufacturer or importer shall provide notifications in addition to those described in subparagraph (A), as necessary, to device user facilities or health professionals through the electronic notification format established under subsection (a). (c) Electronic database The Secretary shall maintain an electronic database that is publicly accessible, downloadable, and populated with information regarding device notifications made under this section. (d) Definitions In this section and in section 518C\u2014 (1) the term device user facility has the meaning given such term in section 519(b)(6); and (2) the term recall has the meaning given such term in section 518A. (e) Authorization of appropriations For purposes of conducting activities under this section and hiring personnel to conduct such activities, there is authorized to be appropriated $6,700,000 for fiscal year 2026, $1,700,000 for fiscal year 2027, and $1,000,000 for each of fiscal years 2028 through 2030, to remain available until expended, without fiscal year limitation. 518C. Patient notification (a) In general The Secretary shall require that any recall strategy under section 519(g) provides for notice to patients whom device user facilities and health professionals treated with the device. (b) Compliance In accordance with subsection (a), the Secretary shall require recall notifications sent from the manufacturer or importer of the device to\u2014 (1) include information for device user facilities and health professionals about the risks presented by the device to patients whom device user facilities and health professionals treated with the device; and (2) instruct such device user facilities and health professionals to share information under paragraph (1) with patients whom device user facilities and health professionals treated with the device. (c) Affected devices Subsection (a) shall apply with respect to any class I or class II recall for a class II or class III device that is used outside of device user facilities and\u2014 (1) implanted in the human body; (2) life-sustaining; (3) life-supporting; or (4) used significantly in pediatric populations. (d) Rule of construction Nothing in this section shall be construed to require device user facilities or health professionals to provide patient information to the manufacturer or importer of the device. .\n#### 3. Prohibited acts\nSection 301 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331 ) is amended by adding at the end the following:\n(jjj) The refusal or failure to submit notifications in accordance with paragraphs (1) and (2) of section 518B(b). (kkk) The refusal or failure to provide notice in accordance with section 518C. .",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-12-10",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S8625)"
      },
      "number": "3421",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Medical Device Recall Improvement Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-01-07T17:50:36Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6594ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve medical device recall notifications by amending the Federal Food, Drug, and Cosmetic Act to establish an electronic format for device recall notifications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:24Z"
    },
    {
      "title": "Medical Device Recall Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medical Device Recall Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    }
  ]
}
```
