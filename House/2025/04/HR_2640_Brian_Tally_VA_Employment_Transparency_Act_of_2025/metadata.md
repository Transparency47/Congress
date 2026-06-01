# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2640?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2640
- Title: Brian Tally VA Employment Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2640
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-12-12T09:07:34Z
- Update date including text: 2025-12-12T09:07:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-11 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-11 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2640",
    "number": "2640",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Brian Tally VA Employment Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:34Z",
    "updateDateIncludingText": "2025-12-12T09:07:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-11",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-11T15:35:06Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2640ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2640\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Luttrell introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to ensure that certain health care contractors of the Department of Veterans Affairs are subject to Federal tort claims laws, to improve the accountability of physicians of the Department, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Brian Tally VA Employment Transparency Act of 2025 .\n#### 2. Accountability of health care providers at facilities of the Department of Veterans Affairs\n##### (a) Treatment of contractors under Federal tort claims laws\nSection 7316 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(g) (1) (A) This section shall not apply with respect to civil actions or other proceedings brought by an individual, or the estate of an individual, for damages for personal injury, including death, allegedly arising from the malpractice or negligence of a non-Department provider in the course of providing hospital care, medical services, or nursing home care at a facility of the Department, if the Secretary provides to the individual, or the estate of the individual, by not later than 45 days after the Secretary receives notice of the civil action or other proceeding, the information referred to in subparagraph (B). (B) The information referred to in this subparagraph is the following: (i) A description of the extent of the involvement of the non-Department provider in the hospital care, medical services, or nursing home care furnished to the individual. (ii) The nature of such care or services furnished to the individual by the non-Department provider. (iii) The full name of the non-Department provider. (iv) The fact that the notification is made pursuant to this paragraph. (C) A civil action or other proceeding arising from an incident of alleged malpractice or negligence of a non-Department provider may not be brought in both a State court and in a Federal court. (2) (A) If five or more separate covered cases brought during a five-year period include allegations of malpractice or negligence on the part of any individual non-Department provider, the Secretary\u2014 (i) shall revoke the provider\u2019s authorization to provide hospital care, medical services, or nursing home care at a facility of the Department; and (ii) may not enter into any contract or agreement that authorizes the provider to provide such care or services at a facility of the Department. (B) The Secretary shall establish a process by which a non-Department provider may appeal an action under subparagraph (A). (3) In this subsection: (A) The term covered case means any of the following: (i) A civil action or proceeding pursuant to this section that resulted in a judgment against the United States, or such an action or proceeding that the United States compromises or settles. (ii) A civil action or proceeding pursuant to State law for personal injury, including death, allegedly arising from malpractice or negligence that resulted in a judgment against a non-Department provider, or such an action or proceeding that the non-Department provider compromises or settles. (B) The term non-Department provider \u2014 (i) means a health care provider who is not an employee of the Federal Government but who is authorized by the Secretary to provide health care or treatment at a facility of the Department pursuant to a contract or other agreement; and (ii) does not include a provider through which the Secretary furnishes care or services under section 1703 of this title. .\n##### (b) Notifications and outreach regarding Federal tort claims\nSuch section, as amended by subsection (a), is further amended by adding at the end the following new subsections:\n(h) Not later than 30 days following the date on which a judgment is entered against the United States in a civil action or proceeding pursuant to this section that includes a conclusion that a non-Department employee committed negligence or malpractice, the Secretary shall notify the following entities with respect to such judgment: (1) The appropriate licensing entity of each State in which such non-Department employee is licensed as a health care professional. (2) The National Practitioner Data Bank established pursuant to the Health Care Quality Improvement Act of 1986 ( 42 U.S.C. 11101 et seq. ). (i) The Secretary shall publish in a clear and conspicuous manner on the internet website of the Department an explanation of the rights of an individual under this section, including\u2014 (1) an explanation of the procedure to file an administrative claim pursuant to section 515 of this title or section 2675 of title 28; (2) the circumstances under which an individual may file a civil action or proceeding pursuant to this section; and (3) time limits that can bar recovery under this section. .\n##### (c) Accountability of physicians of the Department\nSection 7461 of such title is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby inserting (1) before Whenever ; and\n**(B)**\nby adding at the end the following new paragraph:\n(2) The Under Secretary shall bring charges under paragraph (1) based on professional conduct or competence against a section 7401(1) employee who is accused of committing negligence or malpractice in three or more separate civil actions or proceedings pursuant to section 7316 of this title within a five-year period if such actions or proceedings\u2014 (A) resulted in a judgment against the United States; or (B) were compromised or settled by the United States. ; and\n**(2)**\nin subsection (c)(3), by adding at the end the following new subparagraph:\n(C) The provision of care subject to a civil action or proceeding pursuant to section 7316 of this title that\u2014 (i) resulted in a judgment against the United States; or (ii) is compromised or settled by the United States. .\n##### (d) Applicability\nThe amendments made by this section shall take effect with respect to actions or omissions covered under section 7316 of title 38, United States Code, occurring on or after the date of the enactment of this Act.",
      "versionDate": "2025-04-03",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T14:09:09Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2640ih.xml"
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
      "title": "Brian Tally VA Employment Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T10:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Brian Tally VA Employment Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T10:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to ensure that certain health care contractors of the Department of Veterans Affairs are subject to Federal tort claims laws, to improve the accountability of physicians of the Department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T10:18:19Z"
    }
  ]
}
```
