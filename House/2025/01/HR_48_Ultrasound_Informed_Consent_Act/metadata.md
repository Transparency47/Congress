# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/48?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/48
- Title: Ultrasound Informed Consent Act
- Congress: 119
- Bill type: HR
- Bill number: 48
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-04T19:59:09Z
- Update date including text: 2025-03-04T19:59:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/48",
    "number": "48",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Ultrasound Informed Consent Act",
    "type": "HR",
    "updateDate": "2025-03-04T19:59:09Z",
    "updateDateIncludingText": "2025-03-04T19:59:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:10:50Z",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MO"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr48ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 48\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Crenshaw , and Mr. Burlison ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to ensure that women seeking an abortion receive an ultrasound and the opportunity to review the ultrasound before giving informed consent to receive an abortion.\n#### 1. Short title\nThis Act may be cited as the Ultrasound Informed Consent Act .\n#### 2. Amendment to the Public Health Service Act\nThe Public Health Service Act ( 42 U.S.C. 201 et seq. ) is amended by adding at the end the following:\nXXXIV INFORMED CONSENT 3401. Definitions In this title: (1) Abortion The term abortion means the intentional use or prescription of any instrument, medicine, drug, substance, device, or method to terminate the life of an unborn child, or to terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (A) to produce a live birth and preserve the life and health of the child after live birth; or (B) to remove an ectopic pregnancy, or to remove a dead unborn child who died as the result of a spontaneous abortion, accidental trauma, or a criminal assault on the pregnant female or her unborn child. (2) Abortion provider The term abortion provider means any person legally qualified to perform an abortion under applicable Federal and State laws. (3) Unborn child The term unborn child means a member of the species homo sapiens, at any stage of development prior to birth. (4) Unemancipated minor The term unemancipated minor means a minor who is subject to the control, authority, and supervision of his or her parent or guardian, as determined under State law. (5) Woman The term woman means a female human being whether or not she has reached the age of majority. 3402. Requirement of informed consent (a) Requirement of compliance by providers Any abortion provider in or affecting interstate or foreign commerce, who knowingly performs any abortion, shall comply with the requirements of this title. (b) Performance and review of ultrasound Prior to a woman giving informed consent to having any part of an abortion performed, the abortion provider who is to perform the abortion, or an agent under the supervision of the provider, shall\u2014 (1) perform an obstetric ultrasound on the pregnant woman; (2) provide a simultaneous explanation of what the ultrasound is depicting; (3) display the ultrasound images so that the pregnant woman may view them; and (4) provide a complete medical description of the ultrasound images, which shall include\u2014 (A) the dimensions of the embryo or fetus; (B) cardiac activity if present and visible; and (C) the presence of external members and internal organs if present and viewable. (c) Ability To turn eyes away Nothing in this section shall be construed to prevent a pregnant woman from turning her eyes away from the ultrasound images required to be displayed and described to her. Neither the abortion provider nor the pregnant woman shall be subject to any penalty under this title if the pregnant woman declines to look at the displayed ultrasound images. 3403. Exception for medical emergencies (a) Exception The provisions of section 3402 shall not apply to an abortion provider if the abortion is necessary to save the life of a mother whose life is endangered by a physical disorder, physical illness, or physical injury, including a life-endangering physical condition caused by or arising from the pregnancy itself. (b) Certification Upon a determination by an abortion provider under subsection (a) that an abortion is necessary to save the life of a mother, such provider shall include in the medical file of the pregnant woman a truthful and accurate certification of the specific medical circumstances that support such determination. 3404. Penalties for failure to comply (a) Civil penalties (1) In general The Attorney General may commence a civil action in Federal court under this section against any abortion provider who knowingly commits an act constituting a violation of this title for a penalty in an amount not to exceed\u2014 (A) $100,000 for each such violation that is adjudicated in the first proceeding against such provider under this title; and (B) $250,000 for each violation of this title that is adjudicated in a subsequent proceeding against such provider under this title. (2) Notification Upon the assessment of a civil penalty under paragraph (1), the Attorney General shall notify the appropriate State medical licensing authority. (b) Private right of action A woman upon whom an abortion has been performed in violation of this title may commence a civil action against the abortion provider for any violation of this title for actual and punitive damages. For purposes of the preceding sentence, actual damages are objectively verifiable money damages for all injuries. .\n#### 3. Preemption\nNothing in this Act or the amendment made by this Act shall be construed to preempt any provision of State law to the extent that such State law establishes, implements, or continues in effect disclosure requirements regarding abortion or penalties for failure to comply with such requirements that are more extensive than those provided under the amendment made by this Act.\n#### 4. Severability\nIf any provision of this Act or the amendment made by this Act, or any application thereof, is found to be unconstitutional, the remainder of this Act and the amendment made by this Act, and any application thereof, shall not be affected by such finding.",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-02-10T20:49:41Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-10T20:49:41Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-02-10T20:49:41Z"
          },
          {
            "name": "Medical ethics",
            "updateDate": "2025-02-10T20:49:41Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-02-10T20:49:41Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-02-10T20:49:41Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-02-10T20:49:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-04T12:21:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr48",
          "measure-number": "48",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr48v00",
            "update-date": "2025-03-04"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ultrasound Informed Consent Act</strong></p><p>This bill requires abortion providers to conduct an ultrasound before performing an abortion.</p><p>Specifically, before a woman gives informed consent to any part of an abortion, the abortion provider must</p><ul><li>perform an obstetric ultrasound on the pregnant woman;</li><li>provide a simultaneous explanation of what the ultrasound is depicting;</li><li>display the ultrasound images so the woman may view them; and</li><li>provide a complete medical description of the images, including the dimensions of the embryo or fetus, cardiac activity if present and visible, and the presence of external members and internal organs if present and viewable.</li></ul><p>Providers are subject to civil actions and penalties for violations.</p><p>The bill's ultrasound requirements do not apply in cases where a physical disorder, illness, or injury endangers a woman's life. A woman is also not required to view the ultrasound images; nor may she or the provider be penalized if she declines to do so.</p>"
        },
        "title": "Ultrasound Informed Consent Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr48.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ultrasound Informed Consent Act</strong></p><p>This bill requires abortion providers to conduct an ultrasound before performing an abortion.</p><p>Specifically, before a woman gives informed consent to any part of an abortion, the abortion provider must</p><ul><li>perform an obstetric ultrasound on the pregnant woman;</li><li>provide a simultaneous explanation of what the ultrasound is depicting;</li><li>display the ultrasound images so the woman may view them; and</li><li>provide a complete medical description of the images, including the dimensions of the embryo or fetus, cardiac activity if present and visible, and the presence of external members and internal organs if present and viewable.</li></ul><p>Providers are subject to civil actions and penalties for violations.</p><p>The bill's ultrasound requirements do not apply in cases where a physical disorder, illness, or injury endangers a woman's life. A woman is also not required to view the ultrasound images; nor may she or the provider be penalized if she declines to do so.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119hr48"
    },
    "title": "Ultrasound Informed Consent Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ultrasound Informed Consent Act</strong></p><p>This bill requires abortion providers to conduct an ultrasound before performing an abortion.</p><p>Specifically, before a woman gives informed consent to any part of an abortion, the abortion provider must</p><ul><li>perform an obstetric ultrasound on the pregnant woman;</li><li>provide a simultaneous explanation of what the ultrasound is depicting;</li><li>display the ultrasound images so the woman may view them; and</li><li>provide a complete medical description of the images, including the dimensions of the embryo or fetus, cardiac activity if present and visible, and the presence of external members and internal organs if present and viewable.</li></ul><p>Providers are subject to civil actions and penalties for violations.</p><p>The bill's ultrasound requirements do not apply in cases where a physical disorder, illness, or injury endangers a woman's life. A woman is also not required to view the ultrasound images; nor may she or the provider be penalized if she declines to do so.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119hr48"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr48ih.xml"
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
      "title": "Ultrasound Informed Consent Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T11:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ultrasound Informed Consent Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to ensure that women seeking an abortion receive an ultrasound and the opportunity to review the ultrasound before giving informed consent to receive an abortion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T11:18:28Z"
    }
  ]
}
```
