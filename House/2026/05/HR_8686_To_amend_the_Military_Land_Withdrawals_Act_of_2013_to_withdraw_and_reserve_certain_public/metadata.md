# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8686
- Title: To amend the Military Land Withdrawals Act of 2013 to withdraw and reserve certain public land in the vicinity of Yuma Proving Ground, Arizona.
- Congress: 119
- Bill type: HR
- Bill number: 8686
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-27T08:05:59Z
- Update date including text: 2026-05-27T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-05-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8686",
    "number": "8686",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "To amend the Military Land Withdrawals Act of 2013 to withdraw and reserve certain public land in the vicinity of Yuma Proving Ground, Arizona.",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:59Z",
    "updateDateIncludingText": "2026-05-27T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-05-21T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-05-12T21:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-07T13:06:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8686ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8686\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Gosar introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Military Land Withdrawals Act of 2013 to withdraw and reserve certain public land in the vicinity of Yuma Proving Ground, Arizona.\n#### 1. Withdrawal and reservation of lands located on the Yuma Proving Ground, Arizona, to support military readiness and security\nThe Military Land Withdrawals Act of 2013 (title XXIX of Public Law 113\u201366 ; 127 Stat. 1025) is amended by adding at the end the following new subtitle:\nH Yuma Proving Ground, Arizona 2999B. Withdrawal and reservation of public land (a) Withdrawal Subject to valid existing rights and except as otherwise provided in this subtitle, the public land (including interests in the land) described in subsection (b), and all other areas within the boundary of the land depicted on the map described in that subsection that may become subject to the operation of the public land laws, is withdrawn from\u2014 (1) all forms of entry, appropriation, and disposal under the public land laws; (2) location, entry, and patent under the mining laws; and (3) disposition under all laws relating to mineral and geothermal leasing. (b) Description of land The public land (including interests in the land) referred to in subsection (a) consists of\u2014 (1) the approximately 21,782.981 acres of Federal land\u2014 (A) generally depicted as Highway 95 - Requested Withdrawal Area on of the map titled U.S. Army Yuma Proving Ground Withdrawal Highway 95 Withdrawal Area , sheet 2 of 3, dated March 12, 2025; and (B) excluding the approximately 800 acres of subsurface estate owned by the State of Arizona within the area generally depicted as Surface Only Withdrawal/Subsurface Owned by Non-Federal Entity on the map described in subparagraph (A); and (2) the approximately 249.29 acres of Federal land generally depicted as Howard Cantonment - Requested Withdrawal Area on the map titled U.S. Army Yuma Proving Ground Withdrawal Howard Cantonment Withdrawal Area , sheet 3 of 3, dated March 12, 2025. (c) Reservation; purpose The land described in subsection (b) is reserved for use by the Secretary of the Army for the purposes specified in Public Land Order No. 848 of July 1, 1952, and as authorized under section 2914. 2999C. Management of withdrawn and reserved land (a) Applicable laws The Secretary of the Interior shall manage the land withdrawn and reserved by section 2999B in accordance with\u2014 (1) subtitle A and this subtitle; (2) the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); and (3) any other applicable law. (b) Authorized activities To the extent consistent with applicable law and Executive orders, the land withdrawn and reserved by section 2999B may be managed in a manner that permits the following activities: (1) Conservation of wildlife and wildlife habitat. (2) Preservation of cultural properties. (3) Management of wild horses and burros. (4) Control of predatory and other animals. (5) Recreation, public access, and hunting. (6) Prevention and appropriate suppression of brush and range fires resulting from non-military activities. (c) Nondefense uses Subject to subsection (d), all nondefense-related uses of the land withdrawn and reserved by section 2999B, shall be subject to any conditions and restrictions that the Secretary of the Interior and the Secretary of the Army jointly determine to be necessary to permit the defense-related use of the land for the purposes described in this section. (d) Issuance of leases and other land use authorizations (1) In general The Secretary of the Interior shall be responsible for the issuance of any lease, easement, right-of-way, permit, license, or other instrument authorized by law with respect to any activity that traverses both\u2014 (A) the public land withdrawn and reserved by section 2999B; and (B) any other land in the vicinity of the land withdrawn and reserved by section 2999B that is not under the administrative jurisdiction of the Secretary of the Army. (2) Consent required Except as specified in section 2999E, any lease, easement, right-of-way, permit, license, or other instrument issued under paragraph (1) shall\u2014 (A) only be issued with the consent of the Secretary of the Army; and (B) be subject to such conditions as the Secretary of the Army may require with respect to the land withdrawn and reserved by section 2999B. 2999D. Assignment of management responsibility to Secretary of the Army (a) Authority To assign management responsibility The Secretary of the Interior may assign the management responsibilities for the land withdrawn and reserved by section 2999B to the Secretary of the Army. (b) Applicable law On assignment of the management responsibility under subsection (a), the Secretary of the Army shall manage the land in accordance with\u2014 (1) subtitle A and this subtitle; (2) title I of the Sikes Act ( 16 U.S.C. 670a et seq. ); (3) the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); (4) cooperative management arrangements entered into by the Secretary of the Interior and the Secretary of the Army; and (5) any other applicable law. 2999E. Utility corridor (a) Issuance of utility rights-of-Way Notwithstanding subsections (c) and (d) of section 2999C, the Secretary of the Interior may issue rights-of-way within the Bureau of Land Management designated Parker-Blaisdell Utility Corridor under the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ) for any critical regional-grid level utility infrastructure to include above-ground transmission lines, consistent with the Memorandum of Understanding between the United States Department of the Interior Bureau of Land Management Yuma Field Office and United States Army Garrison Yuma Regarding the Yuma Proving Ground Highway 95 Withdrawal, dated February 28, 2025. (b) Limitation on delegation The authority to issue a right-of-way under subsection (a) may not be delegated below the level of the Bureau of Land Management State Director. (c) Army consent not required The decision to issue a right-of-way under subsection (a) is not subject to consent by the Secretary of the Army; however, the Secretary of the Interior, in consultation with the Secretary of the Army, shall incorporate conditions in any right-of-way issued under subsection (a) as much as practicable to minimize impacts to the mission of the Army. (d) Limitation The authority to issue rights-of-way under subsection (a) may not be assigned to the Secretary of the Army. 2999F. Duration of withdrawal and reservation The withdrawal and reservation of public land made by section 2999B shall be in effect for\u2014 (1) an indefinite period; or (2) until the Secretary of the Army determines that there is no longer a military need for the withdrawal and reservation. .",
      "versionDate": "2026-05-07",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-15T18:22:11Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8686ih.xml"
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
      "title": "To amend the Military Land Withdrawals Act of 2013 to withdraw and reserve certain public land in the vicinity of Yuma Proving Ground, Arizona.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T03:18:40Z"
    },
    {
      "title": "To amend the Military Land Withdrawals Act of 2013 to withdraw and reserve certain public land in the vicinity of Yuma Proving Ground, Arizona.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:06:00Z"
    }
  ]
}
```
