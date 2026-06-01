# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8557?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8557
- Title: Short-Term Holding Facility Standards Restoration Act.
- Congress: 119
- Bill type: HR
- Bill number: 8557
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-19T21:50:37Z
- Update date including text: 2026-05-19T21:50:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8557",
    "number": "8557",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Short-Term Holding Facility Standards Restoration Act.",
    "type": "HR",
    "updateDate": "2026-05-19T21:50:37Z",
    "updateDateIncludingText": "2026-05-19T21:50:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "AZ"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "AZ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8557ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8557\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mr. Stanton (for himself, Ms. Ansari , and Mrs. Grijalva ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit long-term custody in U.S. Immigration and Customs Enforcement holding facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Short-Term Holding Facility Standards Restoration Act.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nU.S. Immigration and Customs Enforcement holding facilities are designed for short-term custody and processing.\n**(2)**\nPrior U.S. Immigration and Customs Enforcement policy defined short-term as not exceeding 12 hours, absent exceptional circumstances.\n**(3)**\nProlonged detention in holding facilities undermines detainee welfare, facility design limits, and operational intent.\n**(4)**\nRestoring the 12-hour standard ensures consistency with prior agency guidance.\n#### 3. Limitation on duration of detention\n##### (a) In general\nThe Secretary of Homeland Security shall ensure that, absent exceptional circumstances described in subsection (b), a U.S. Immigration and Customs Enforcement holding facility may only be used for short-term custody of a detainee.\n##### (b) Exceptional circumstances\nExceptional circumstances are temporary and unforeseen circumstances requiring immediate action, including\u2014\n**(1)**\nmedical emergencies;\n**(2)**\nnatural disasters or facility disruptions;\n**(3)**\ntransportation or transfer delays beyond the control of the Department of Homeland Security; or\n**(4)**\nother exigent operational conditions as determined by the Secretary of Homeland Security.\n#### 4. Humane conditions\nThe Secretary of Homeland Security shall ensure that\u2014\n**(1)**\neach U.S. Immigration and Customs Enforcement holding facility is safe, clean, equipped with restroom facilities, and clear of any object that could be used as a weapon; and\n**(2)**\neach detainee in such facility\u2014\n**(A)**\nis provided a meal not less than every 6 hours;\n**(B)**\nin the case of a minor, pregnant woman, or breastfeeding woman, is provided immediate access to meals, snacks, milk, and juice, without regard to the amount of time in custody; and\n**(C)**\nis provided with access to drinking water in each room in which a detainee is held at all times.\n#### 5. Documentation and compliance\n##### (a) Documentation\nThe Secretary of Homeland Security shall require contemporaneous documentation of any instance in which a detainee is held in a U.S. Immigration and Customs Enforcement holding facility for custody other than short-term custody.\n##### (b) Retention\nRecords under this section shall be maintained for oversight, audit, and reporting purposes for a period of 5 years.\n#### 6. Oversight and reporting\n##### (a) Annual report\nThe Secretary of Homeland Security shall submit to Congress an annual report detailing\u2014\n**(1)**\nthe number of detainees held in custody other than short-term custody in a U.S. Immigration and Customs Enforcement holding facility;\n**(2)**\nthe duration of such custody;\n**(3)**\nthe justification for each instance in which a detainee is held in a U.S. Immigration and Customs Enforcement holding facility for custody other than short-term custody; and\n**(4)**\ncorrective actions taken to ensure compliance.\n##### (b) Inspector General review\nThe Inspector General of the Department of Homeland Security shall perform periodic audits of U.S. Immigration and Customs Enforcement holding facilities and Department of Homeland Security records to ensure compliance with this Act.\n#### 7. Definitions\nFor the purposes of this Act\u2014\n**(1)**\nthe term holding facility means any facility or holding room for temporary custody, processing, or transfer, and not designed for long-term detention; and\n**(2)**\nthe term short-term custody means detention in a holding facility for a period not to exceed 12 hours, absent exceptional circumstances.",
      "versionDate": "2026-04-28",
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
        "name": "Immigration",
        "updateDate": "2026-05-19T21:50:37Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8557ih.xml"
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
      "title": "Short-Term Holding Facility Standards Restoration Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Short-Term Holding Facility Standards Restoration Act.",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit long-term custody in U.S. Immigration and Customs Enforcement holding facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:37Z"
    }
  ]
}
```
