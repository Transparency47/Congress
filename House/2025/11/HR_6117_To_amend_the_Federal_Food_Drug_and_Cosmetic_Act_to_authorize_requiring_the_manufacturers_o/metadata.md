# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6117
- Title: Patient Device Data Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6117
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-12-04T15:47:45Z
- Update date including text: 2025-12-04T15:47:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6117",
    "number": "6117",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Patient Device Data Access Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-04T15:47:45Z",
    "updateDateIncludingText": "2025-12-04T15:47:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:06:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6117ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6117\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Ms. Sherrill introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to authorize requiring the manufacturers of a covered device to disclose to a patient all patient-specific data that is recorded or transmitted by the device and accessible to the manufacturer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Patient Device Data Access Act of 2025 .\n#### 2. Sharing of patient-specific data by device manufacturers\n##### (a) In general\nSubchapter A of chapter V of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 351 et seq. ) is amended by adding at the end the following:\n524C. Sharing of patient-specific data by device manufacturers (a) Requirement authorized The Secretary may require the manufacturer of a covered device, at the request of a patient who is using or has used such covered device, to disclose all patient-specific data that is\u2014 (1) recorded or transmitted by such device; and (2) accessible to the manufacturer. (b) Regulations (1) Issuance Any requirement imposed on manufacturers under subsection (a) shall be by regulation. (2) Applicability to all manufacturers of covered devices Any requirement imposed under subsection (a) shall be applicable with respect to all manufacturers of covered devices. (3) Consideration In issuing any regulation under paragraph (1), the Secretary shall take into consideration the guidance issued in October 2017 by the Food and Drug Administration titled Manufacturers Sharing Patient-Specific Information from Medical Devices with Patients Upon Request . (4) Contents If the Secretary issues regulations under paragraph (1), the Secretary may include in such regulations provisions requiring the manufacturer of a covered device to do the following: (A) At the request of a patient, disclose patient-specific data referred to in subsection (a), where possible\u2014 (i) in a format that is understandable to the patient; and (ii) to the extent practicable, in a format preferred by the patient. (B) Publish on the public website of the manufacturer of a covered device\u2014 (i) an indication that such device is a covered device subject to regulation under this section; (ii) what types of patient-specific data, if any, are\u2014 (I) being recorded or transmitted by the covered device; and (II) accessible to the manufacturer; and (iii) whether and how the manufacturer utilizes patient data, not including any proprietary information of the manufacturer. (C) Make publicly available, by posting on the manufacturer\u2019s website, the method by which patients who are using or have used the covered device may request their own patient-specific data described in subsection (a). (D) Notify, where possible, patients who are using or have used the covered device about how they can access patient-specific data described in subsection (a). (E) Notify patients if their covered device is subject to a recall, has a software update, or has generated an error message. (c) Exceptions This section does not authorize the Secretary to require the manufacturer of a covered device\u2014 (1) to disclose data that is\u2014 (A) recorded, transmitted, and retained in a closed system; and (B) inaccessible to the manufacturer; (2) to redesign the covered device to enable disclosure of patient-specific data; or (3) to disclose patient-specific data that is inaccessible to the manufacturer. (d) Definitions In this section: (1) The term covered device means any electronic device that is\u2014 (A) intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease; (B) implanted into a patient\u2019s body; (C) used for the purposes of remote monitoring; and (D) capable of recording or transmitting patient data. (2) The term patient-specific data \u2014 (A) means data unique to an individual patient or unique to the patient\u2019s treatment or diagnosis that is recorded or transmitted by a covered device; (B) includes data described in subparagraph (A) irrespective of whether such data, absent regulation under this section, would otherwise be required by law to be disclosed to the patient or their physician; and (C) shall include\u2014 (i) information recorded by a covered device regarding usage, alarms, or outputs; and (ii) pulse oximetry data, heart electrical activity data, and data on rhythms as monitored by a pace maker. (3) The term inaccessible to the manufacturer means data that is not reasonably accessible. .\n##### (b) Civil penalties\nSection 303(f)(1)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333(f)(1)(A) ) is amended by inserting , including any such requirement under section 524C, after a requirement of this Act which relates to devices .",
      "versionDate": "2025-11-18",
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
        "name": "Health",
        "updateDate": "2025-12-04T15:47:45Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6117ih.xml"
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
      "title": "Patient Device Data Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T10:08:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Patient Device Data Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T10:08:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to authorize requiring the manufacturers of a covered device to disclose to a patient all patient-specific data that is recorded or transmitted by the device and accessible to the manufacturer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T10:03:31Z"
    }
  ]
}
```
