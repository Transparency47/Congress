# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3027
- Title: Green Star Families Act
- Congress: 119
- Bill type: HR
- Bill number: 3027
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-12-12T09:08:10Z
- Update date including text: 2025-12-12T09:08:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3027",
    "number": "3027",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Green Star Families Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:08:10Z",
    "updateDateIncludingText": "2025-12-12T09:08:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
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
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-12T15:48:49Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3027ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3027\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish a counseling program for certain survivors of veterans who die by suicide.\n#### 1. Short title\nThis Act may be cited as the Green Star Families Act .\n#### 2. Counseling program for next of kin and caregivers of veterans who die by suicide\n##### (a) Establishment\nSubchapter II of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section (and amending the table of sections at the beginning of such chapter accordingly):\n1720M. Counseling program for next of kin and caregivers of veterans who die by suicide (a) Counseling program (1) Subject to paragraph (2), the Secretary shall furnish, at no cost to the recipient, counseling services to\u2014 (A) the next of kin of a veteran who dies by suicide; and (B) a former volunteer caregiver of a veteran who dies by suicide. (2) The Secretary may provide counseling services under this section only if the Secretary determines such counseling services are\u2014 (A) reasonably accessible to an individual described in paragraph (1); and (B) substantially equivalent or superior to similar services furnished by the Secretary to an individual described in paragraph (1). (3) To carry out subsection (a), the Secretary may enter into an agreement with a Federal, State, or private entity. The Secretary may provide fair compensation to such entity pursuant to such agreement. (b) Public awareness In carrying out the program under subsection (a), the Secretary shall\u2014 (1) publish information relating to the program on a website of the Department; and (2) provide information relating to the program to any individual described in paragraph (1). (c) Definitions In this section: (1) The term covered veterans service organization includes\u2014 (A) an organization recognized by the Secretary for the representation of veterans under section 5902 of this title; and (B) an organization\u2014 (i) that is described in section 501(c)(3) or 501(c)(19) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code; and (ii) that carries out activities relating to veterans and their assistance. (2) The term former volunteer caregiver means, with respect to a veteran who dies by suicide, an individual\u2014 (A) who is at least 18 years of age; and (B) who, prior to the death of the veteran, and in connection with a covered veterans service organization, furnished the veteran with counseling, social work, or other personal care services\u2014 (i) without compensation to such individual; and (ii) for a period of at least three months. (3) The term next of kin means the closest living relative of a veteran who dies by suicide, in the following order of priority: (A) Spouse. (B) A child. (C) A parent. (D) A sibling. (E) Another individual determined by the Secretary. (4) The term personal care services has the meaning given such term in section 1720G of this title. .\n##### (b) Implementation deadline\nThe Secretary of Veterans Affairs shall carry out section 1720M of such title, as added by subsection (a), not later than 90 days after the date of the enactment of this Act.",
      "versionDate": "2025-04-24",
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
        "updateDate": "2025-05-28T20:52:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-24",
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
          "measure-id": "id119hr3027",
          "measure-number": "3027",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-24",
          "originChamber": "HOUSE",
          "update-date": "2025-08-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3027v00",
            "update-date": "2025-08-07"
          },
          "action-date": "2025-04-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Green Star Families Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish free counseling services to the next of kin and former volunteer caregivers of veterans who die by suicide. (Generally, Green Star families are families of servicemembers and veterans who have died by suicide.)</p><p>The VA may provide counseling services under this bill only if the services are reasonably accessible to the eligible individuals and are substantially equivalent or superior to similar services furnished by the VA to such individuals.</p><p>The VA is authorized to enter into an agreement with a federal, state, or private entity to provide the counseling services.</p><p>Additionally, the VA must publish information relating to the program online and provide information relating to the program to any eligible individual.</p>"
        },
        "title": "Green Star Families Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3027.xml",
    "summary": {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Green Star Families Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish free counseling services to the next of kin and former volunteer caregivers of veterans who die by suicide. (Generally, Green Star families are families of servicemembers and veterans who have died by suicide.)</p><p>The VA may provide counseling services under this bill only if the services are reasonably accessible to the eligible individuals and are substantially equivalent or superior to similar services furnished by the VA to such individuals.</p><p>The VA is authorized to enter into an agreement with a federal, state, or private entity to provide the counseling services.</p><p>Additionally, the VA must publish information relating to the program online and provide information relating to the program to any eligible individual.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr3027"
    },
    "title": "Green Star Families Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Green Star Families Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish free counseling services to the next of kin and former volunteer caregivers of veterans who die by suicide. (Generally, Green Star families are families of servicemembers and veterans who have died by suicide.)</p><p>The VA may provide counseling services under this bill only if the services are reasonably accessible to the eligible individuals and are substantially equivalent or superior to similar services furnished by the VA to such individuals.</p><p>The VA is authorized to enter into an agreement with a federal, state, or private entity to provide the counseling services.</p><p>Additionally, the VA must publish information relating to the program online and provide information relating to the program to any eligible individual.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr3027"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3027ih.xml"
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
      "title": "Green Star Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Green Star Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to establish a counseling program for certain survivors of veterans who die by suicide.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:18:18Z"
    }
  ]
}
```
