# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2878?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2878
- Title: Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act
- Congress: 119
- Bill type: HR
- Bill number: 2878
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-05-27T08:06:11Z
- Update date including text: 2026-05-27T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-01-21 - Committee: Subcommittee Hearings Held
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-01-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2878",
    "number": "2878",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:11Z",
    "updateDateIncludingText": "2026-05-27T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-01-21T14:10:30Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-21T14:10:23Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-10T13:04:25Z",
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
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "RI"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "RI"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "HI"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-12",
      "state": "VA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "KY"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CO"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NV"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MD"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "DC"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2878ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2878\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Nunn of Iowa (for himself and Mr. Magaziner ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles 10 and 38, United States Code, to make certain improvements in the Transition Assistance Program and Solid Start Program to address mental health issues, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act .\n#### 2. Addressing mental health issues in the Transition Assistance Program of the Department of Defense and the Solid Start Program of the Department of Veterans Affairs\n##### (a) Transition assistance program of the department of defense\nSection 1142(b) of title 10, United States Code, is amended\u2014\n**(1)**\nin paragraph (5), by inserting (11), before and (16) ; and\n**(2)**\nby striking paragraph (11) and inserting the following:\n(11) Information concerning mental health, including\u2014 (A) the availability of mental health services furnished by the Secretary concerned, the Secretary of Defense, the Secretary of Veterans Affairs, or a non-profit entity; (B) the treatment of post-traumatic stress disorder, traumatic brain injury, anxiety disorders, depression, chronic pain, sleep disorders, suicidal ideation, or other mental health conditions associated with service in the armed forces; (C) the risk of suicide, including signs, symptoms, and risk factors (including adverse childhood experiences, depression, bipolar disorder, homelessness, unemployment, and relationship strain); (D) the availability of treatment options and resources to address substance abuse, including alcohol, prescription drug, and opioid abuse; (E) the potential effects of the loss of community and support systems experienced by a member separating from the armed forces; (F) isolation from family, friends, or society; and (G) the potential stressors associated with separation from the armed forces. .\n##### (b) Solid start program of the department of veterans affairs\nSection 6320(b)(1) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraphs (G) and (H) as subparagraphs (I) and (J), respectively; and\n**(2)**\nby inserting after subparagraph (F) the following new subparagraphs:\n(G) assisting eligible veterans who elect to enroll in the system of patient enrollment under section 1705(a) of this title; (H) educating veterans about mental health and counseling services available through the Veterans Health Administration; .\n##### (c) Report\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense and the Secretary of Veterans Affairs shall jointly submit to the appropriate congressional committees a report on the information and materials developed pursuant to the amendments made by this Act.\n**(2) Appropriate congressional committees defined**\nIn this subsection, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the Senate; and\n**(B)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the House of Representatives.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-06-17",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "2096",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-03-16T16:46:03Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2026-03-16T16:46:03Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2026-03-16T16:46:03Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-03-16T16:46:02Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-03-16T16:46:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T13:57:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2878",
          "measure-number": "2878",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2025-07-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2878v00",
            "update-date": "2025-07-02"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) and Department of Defense (DOD) to provide additional information and assistance related to mental health care to veterans in the Solid Start program and members of the Armed Forces in the Transition Assistance Program.</p><p>Specifically, the bill requires that counseling provided under DOD\u2019s Transition Assistance Program include additional mental health information, including information about the risk of suicide and other potential\u00a0stressors associated with separation from the Armed Forces.</p><p>The bill also expands the activities that must be carried out by the VA under the Solid Start program, which is an outreach program for veterans in their first year of separation from service. Specifically, under the program, the VA must (1) assist eligible veterans who elect to enroll in the VA health care system, and (2) educate veterans about mental health and counseling services available through the Veterans Health Administration.</p>"
        },
        "title": "Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2878.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) and Department of Defense (DOD) to provide additional information and assistance related to mental health care to veterans in the Solid Start program and members of the Armed Forces in the Transition Assistance Program.</p><p>Specifically, the bill requires that counseling provided under DOD\u2019s Transition Assistance Program include additional mental health information, including information about the risk of suicide and other potential\u00a0stressors associated with separation from the Armed Forces.</p><p>The bill also expands the activities that must be carried out by the VA under the Solid Start program, which is an outreach program for veterans in their first year of separation from service. Specifically, under the program, the VA must (1) assist eligible veterans who elect to enroll in the VA health care system, and (2) educate veterans about mental health and counseling services available through the Veterans Health Administration.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr2878"
    },
    "title": "Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) and Department of Defense (DOD) to provide additional information and assistance related to mental health care to veterans in the Solid Start program and members of the Armed Forces in the Transition Assistance Program.</p><p>Specifically, the bill requires that counseling provided under DOD\u2019s Transition Assistance Program include additional mental health information, including information about the risk of suicide and other potential\u00a0stressors associated with separation from the Armed Forces.</p><p>The bill also expands the activities that must be carried out by the VA under the Solid Start program, which is an outreach program for veterans in their first year of separation from service. Specifically, under the program, the VA must (1) assist eligible veterans who elect to enroll in the VA health care system, and (2) educate veterans about mental health and counseling services available through the Veterans Health Administration.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hr2878"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2878ih.xml"
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
      "title": "Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-30T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Daniel J. Harvey, Jr. and Adam Lambert Improving Servicemember Transition to Reduce Veteran Suicide Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-30T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 10 and 38, United States Code, to make certain improvements in the Transition Assistance Program and Solid Start Program to address mental health issues, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-30T03:48:18Z"
    }
  ]
}
```
