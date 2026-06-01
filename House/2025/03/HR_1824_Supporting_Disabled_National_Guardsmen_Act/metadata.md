# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1824?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1824
- Title: Supporting Disabled National Guardsmen Act
- Congress: 119
- Bill type: HR
- Bill number: 1824
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-01-13T09:05:26Z
- Update date including text: 2026-01-13T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1824",
    "number": "1824",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Supporting Disabled National Guardsmen Act",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:26Z",
    "updateDateIncludingText": "2026-01-13T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-04",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T18:01:48Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-04T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NJ"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NJ"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1824ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1824\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mrs. Bice (for herself, Ms. Sherrill , Ms. Houlahan , Mr. Gottheimer , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles 10 and 38, United States Code, to extend certain benefits to members of the National Guard who incur disabilities while performing State active duty.\n#### 1. Short title\nThis Act may be cited as the Supporting Disabled National Guardsmen Act .\n#### 2. Eligibility of a member of the National Guard for retirement from the Armed Forces based on disability incurred while performing State active duty\nSection 1204 of title 10, United States Code, is amended\u2014\n**(1)**\nin paragraph (2)(B)(i)\u2014\n**(A)**\nby striking active duty or inactive-duty training; and inserting an em dash; and\n**(B)**\nby inserting before clause (ii) the following new subclauses:\n(I) active duty; (II) inactive-duty training; or (III) State active duty (as that term is defined in section 4303 of title 38); ;\n**(2)**\nby inserting (a) In general.\u2014 before Upon a determination ; and\n**(3)**\nby adding at the end the following new subsection:\n(b) Limitation In the case of a member retired under this section based on a disability described in subclause (III) of subsection (a)(2)(B)(i), the Secretary concerned shall reduce retired pay, computed under section 1401 of this title and paid to such member, to the extent that the Secretary concerned determines such retired pay duplicates any other Federal or State benefit to such member based on such disability. .\n#### 3. Eligibility of a member of the National Guard who incurs a disability while performing State active duty for health care furnished by the Secretary of Veterans Affairs\n##### (a) Establishment\nSubchapter VIII of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1789A. Health care for members of the National Guard who incur disabilities while performing State active duty (a) In general Subject to subsection (b), a member of the National Guard who incurs a disability while performing State active duty shall be eligible for hospital care and medical services furnished by the Secretary to treat such disability and any illness or condition arising from such disability. (b) Limitation (1) The Secretary may only furnish hospital care and medical services under subsection (a) to the extent and in the amount provided in advance in appropriations Acts for such purpose. (2) The Secretary may provide reimbursement for hospital care or medical services provided to an individual under this section only after the individual or the provider of such care or services has exhausted without success all claims and remedies reasonably available to the individual or provider against a third party (as defined in section 1725(f) of this title) for payment of such care or services, including with respect to health-plan contracts (as defined in such section). (c) State active duty defined In this section, the term State active duty has the meaning given that term in section 4303 of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1789 the following new item:\n1789A. Health care for members of the National Guard who incur disabilities while performing State active duty. .",
      "versionDate": "2025-03-04",
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
        "updateDate": "2025-05-20T02:09:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119hr1824",
          "measure-number": "1824",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-04",
          "originChamber": "HOUSE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1824v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting Disabled National Guardsmen Act</strong></p> <p>This bill provides disability pay and medical care for members of the National Guard who were physically disabled as a result of state active duty.<em> State active duty</em> includes training or other duty in service to the governor of a state for which the member is not entitled to federal pay, but excludes required drills and field exercises.</p> <p>The bill expands eligibility for Department of Defense retired pay to such members who are physically disabled as a result of state active duty after September 23, 1996. Such pay must be reduced if it is determined to duplicate any other federal or state benefit to such members based on disability.</p> <p>The bill also makes such members eligible for hospital care and medical services from the Department of Veterans Affairs (VA) to treat the disability and any illness or condition arising from the disability. The VA may provide reimbursement for hospital care or medical services provided to such members only after a member or the provider of care has exhausted (without success) all claims and remedies reasonably available against a third party.</p>"
        },
        "title": "Supporting Disabled National Guardsmen Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1824.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Disabled National Guardsmen Act</strong></p> <p>This bill provides disability pay and medical care for members of the National Guard who were physically disabled as a result of state active duty.<em> State active duty</em> includes training or other duty in service to the governor of a state for which the member is not entitled to federal pay, but excludes required drills and field exercises.</p> <p>The bill expands eligibility for Department of Defense retired pay to such members who are physically disabled as a result of state active duty after September 23, 1996. Such pay must be reduced if it is determined to duplicate any other federal or state benefit to such members based on disability.</p> <p>The bill also makes such members eligible for hospital care and medical services from the Department of Veterans Affairs (VA) to treat the disability and any illness or condition arising from the disability. The VA may provide reimbursement for hospital care or medical services provided to such members only after a member or the provider of care has exhausted (without success) all claims and remedies reasonably available against a third party.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1824"
    },
    "title": "Supporting Disabled National Guardsmen Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Disabled National Guardsmen Act</strong></p> <p>This bill provides disability pay and medical care for members of the National Guard who were physically disabled as a result of state active duty.<em> State active duty</em> includes training or other duty in service to the governor of a state for which the member is not entitled to federal pay, but excludes required drills and field exercises.</p> <p>The bill expands eligibility for Department of Defense retired pay to such members who are physically disabled as a result of state active duty after September 23, 1996. Such pay must be reduced if it is determined to duplicate any other federal or state benefit to such members based on disability.</p> <p>The bill also makes such members eligible for hospital care and medical services from the Department of Veterans Affairs (VA) to treat the disability and any illness or condition arising from the disability. The VA may provide reimbursement for hospital care or medical services provided to such members only after a member or the provider of care has exhausted (without success) all claims and remedies reasonably available against a third party.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1824"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1824ih.xml"
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
      "title": "Supporting Disabled National Guardsmen Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Disabled National Guardsmen Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 10 and 38, United States Code, to extend certain benefits to members of the National Guard who incur disabilities while performing State active duty.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:24Z"
    }
  ]
}
```
