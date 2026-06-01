# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4218
- Title: CLEAR Act
- Congress: 119
- Bill type: HR
- Bill number: 4218
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-05-01T21:26:23Z
- Update date including text: 2026-05-01T21:26:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-27 - Committee: Referred to the Subcommittee on Environment.
- 2025-12-10 - Committee: Forwarded by Subcommittee to Full Committee by the Yeas and Nays: 14 - 10.
- 2025-12-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-01-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-21 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 23.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-27 - Committee: Referred to the Subcommittee on Environment.
- 2025-12-10 - Committee: Forwarded by Subcommittee to Full Committee by the Yeas and Nays: 14 - 10.
- 2025-12-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-01-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-21 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 23.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4218",
    "number": "4218",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "CLEAR Act",
    "type": "HR",
    "updateDate": "2026-05-01T21:26:23Z",
    "updateDateIncludingText": "2026-05-01T21:26:23Z"
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
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 27 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by the Yeas and Nays: 14 - 10.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
        "item": [
          {
            "date": "2026-01-21T22:26:47Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-27T13:04:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-10T15:32:01Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-10T15:31:31Z",
                "name": "Markup by"
              },
              {
                "date": "2025-06-27T14:31:03Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Environment Subcommittee",
          "systemCode": "hsif18"
        }
      },
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
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "VA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "GA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "OH"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "OH"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "WA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4218ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4218\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Carter of Georgia (for himself, Mr. Griffith , Mr. Allen , Mr. Balderson , Mr. Latta , Mr. Newhouse , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to facilitate State implementation of national ambient air quality standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Air and Economic Advancement Reform Act or the CLEAR Act .\n#### 2. Facilitating State implementation of national ambient air quality standards\n##### (a) Timeline for review of national ambient air quality standards\nParagraphs (1) and (2)(B) of section 109(d) of the Clean Air Act ( 42 U.S.C. 7409(d) ) are amended by striking five-year intervals each place it appears and inserting 10-year intervals .\n##### (b) Consideration of attainability\nSection 109(b)(1) of the Clean Air Act ( 42 U.S.C. 7409(b)(1) ) is amended by inserting after the first sentence the following: If the Administrator, in consultation with the independent scientific review committee appointed under subsection (d), finds that a range of levels of air quality for an air pollutant are requisite to protect public health with an adequate margin of safety, as described in the preceding sentence, the Administrator may, as a secondary consideration in establishing and revising the national primary ambient air quality standard for such air pollutant, consider likely attainability of the standard. .\n##### (c) Opportunity for States To correct deficiency prior to promulgation of Federal implementation plan\nSection 110(c)(1) of the Clean Air Act ( 42 U.S.C. 7410(c)(1) ) is amended\u2014\n**(1)**\nby striking at any time ; and\n**(2)**\nby adding at the end the following: Before promulgating the Federal implementation plan, the Administrator shall give the State at least one year after such finding or disapproval to submit a plan or plan revision to correct the deficiency. If the State submits a plan or plan revision to correct the deficiency, the Administrator may, notwithstanding the 2-year deadline under this paragraph to promulgate a Federal implementation plan, take up to 3 years after such finding or disapproval to promulgate a Federal implementation plan. .\n##### (d) Contingency measures for extreme ozone nonattainment areas\nSection 172(c)(9) of the Clean Air Act ( 42 U.S.C. 7502(c)(9) ) is amended by adding at the end the following: Notwithstanding the preceding sentences and any other provision of this Act, such measures shall not be required for any nonattainment area for ozone classified as an Extreme Area. .\n##### (e) Plan submissions and requirements for ozone nonattainment areas\nSection 182 of the Clean Air Act ( 42 U.S.C. 7511a ) is amended\u2014\n**(1)**\nin subsection (b)(1)(A)(ii)(III), by inserting and economic feasibility after technological achievability ;\n**(2)**\nin subsection (c)(2)(B)(ii), by inserting and economic feasibility after technological achievability ;\n**(3)**\nin subsection (e), in the matter preceding paragraph (1)\u2014\n**(A)**\nby striking The provisions of clause (ii) of subsection (c)(2)(B) (relating to reductions of less than 3 percent), the provisions of paragaphs and inserting The provisions of paragraphs ; and\n**(B)**\nby striking , and the provisions of clause (ii) of subsection (b)(1)(A) (relating to reductions of less than 15 percent) ; and\n**(4)**\nin paragraph (5) of subsection (e), by striking , if the State demonstrates to the satisfaction of the Administrator that\u2014 and all that follows through the end of the paragraph and inserting a period.\n##### (f) Plan revisions for milestones for particulate matter nonattainment areas\nSection 189(c)(1) of the Clean Air Act ( 42 U.S.C. 7513a(c)(1) ) is amended by inserting , which take into account technological achievability and economic feasibility, before and which demonstrate reasonable further progress .\n#### 3. Emissions beyond control\n##### (a) Exceptional events\nSection 319(b) of the Clean Air Act ( 42 U.S.C. 7619(b) ) is amended\u2014\n**(1)**\nin the subsection heading, by inserting Or actions To mitigate wildfire risk after Events ;\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nin the paragraph heading, by striking Definition of exceptional event and inserting Definitions ;\n**(B)**\nin subparagraph (A), by redesignating clauses (i) through (iv), as subclauses (I) through (IV), respectively;\n**(C)**\nby striking (A) and all that follows through an event that\u2014 and inserting the following:\n(A) Exceptional event (i) In general The term exceptional event means an event that\u2014 ;\n**(D)**\nby amending subclause (III) of subparagraph (A)(i), as redesignated, to read as follows:\n(III) is an event that is\u2014 (aa) a natural event; (bb) caused by a human activity that is intended to mirror the occurrence or reoccurrence of a natural event; or (cc) caused by a human activity that is unlikely to recur; and ;\n**(E)**\nby striking subparagraph (B) and inserting the following:\n(ii) Exclusions In this subsection, the term exceptional event does not include\u2014 (I) ordinarily occurring stagnation of air masses; (II) meteorological inversions; or (III) air pollution relating to source noncompliance. ; and\n**(F)**\nby adding at the end the following:\n(B) Action to mitigate wildfire risk The term action to mitigate wildfire risk means a prescribed fire or similar measure, undertaken in accordance with State approved practices, to reduce the risk and severity of wildfires. ;\n**(3)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking March 1, 2006 and inserting 18 months after the date of enactment of the CLEAR Act ;\n**(ii)**\nby inserting revisions to before regulations ; and\n**(iii)**\nby adding or actions to mitigate wildfire risk before the period at the end;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby inserting or action to mitigate wildfire risk after an exceptional event ; and\n**(ii)**\nby striking paragraph (3) and inserting this section ; and\n**(C)**\nby adding at the end the following:\n(C) Regional analysis When more than one State notifies the Administrator of its intent to submit a petition for an exceptional event or an action to mitigate wildfire risk for the same air quality event, the Administrator shall conduct regional modeling and analysis, upon request by one or more States, to satisfy the analysis required for an exceptional event or an action to mitigate wildfire risk petition for such air quality event. (D) Transparency Not later than 12 months after the date of enactment of the CLEAR Act , the Administrator shall establish and update monthly a public website describing the status of all submitted petitions for exceptional events and actions to mitigate wildfire risk. ;\n**(4)**\nin paragraph (3)(A)\u2014\n**(A)**\nby redesignating clauses (ii) through (v) as clauses (iii) through (vi), respectively; and\n**(B)**\nby inserting after clause (i) the following:\n(ii) the principle that actions to mitigate wildfire risk can play an important role in reducing the magnitude and frequency of wildfires; ;\n**(5)**\nin paragraph (3)(B)\u2014\n**(A)**\nin clause (i), by inserting or action to mitigate wildfire risk before must be ;\n**(B)**\nby amending clause (ii) to read as follows:\n(ii) a clear causal relationship must exist, or be reasonably expected to exist, between the measured exceedances of a national ambient air quality standard and the exceptional event or action to mitigate wildfire risk to demonstrate that the exceptional event or action to mitigate wildfire risk caused a specific air pollution concentration at a particular air quality monitoring location; ; and\n**(C)**\nby amending clause (iv) to read as follows:\n(iv) there are criteria and procedures for the Governor of a State to petition the Administrator to exclude air quality monitoring data that is directly due to exceptional events or actions to mitigate wildfire risk from use in determinations by the Administrator with respect to\u2014 (I) area or source exceedances or violations of the national ambient air quality standards; (II) the designation, redesignation, classification, or reclassification of an area; (III) the demonstration by a State of attainment of a national ambient air quality standard; (IV) attainment determinations; (V) attainment date extensions; (VI) finding a State implementation plan to be inadequate; or (VII) preconstruction demonstrations under section 165(a)(3). ; and\n**(6)**\nby striking paragraph (4).\n##### (b) Applicability of sanctions and fees if emissions beyond control\nThe Clean Air Act ( 42 U.S.C. 7401 et seq. ) is amended by inserting after section 179B the following new section:\n179C. Applicability of sanctions and fees if emissions beyond control (a) In general Notwithstanding any other provision of this Act, with respect to any nonattainment area that is classified under section 181 as a Severe Area or an Extreme Area for ozone or under section 188 as a Serious Area for particulate matter, no sanction or fee under section 179 or 185 shall apply with respect to a State (or an area or source therein) on the basis of a deficiency described in section 179(a), or the failure to attain a national ambient air quality standard for ozone or particulate matter by the applicable attainment date, if the State demonstrates that the State would have avoided such deficiency, or such standard would have been attained, but for one or more of the following: (1) Emissions emanating from outside the nonattainment area. (2) Emissions from an exceptional event (as defined in section 319(b)(1)). (3) Emissions from mobile sources to the extent the State demonstrates that\u2014 (A) such emissions are beyond the control of the State to reduce or eliminate; and (B) the State is fully implementing such measures as are within the authority of the State to control emissions from the mobile sources. (b) No effect on underlying standards The inapplicability of sanctions or fees with respect to a State (or an area or source therein) pursuant to subsection (a) does not affect the obligation of a State, area, source, or other entity under other provisions of this Act to establish and implement measures to attain a national ambient air quality standard for ozone or particulate matter. (c) Periodic renewal of demonstration For subsection (a) to continue to apply with respect to a State (or an area or source therein), the State involved shall renew the demonstration required by subsection (a) at least once every 5 years. .\n#### 4. Clean Air Scientific Advisory Committee\n##### (a) Composition of independent scientific review committee\nSection 109(d)(2)(A) of the Clean Air Act ( 42 U.S.C. 7409(d)(2)(A) ) is amended\u2014\n**(1)**\nby striking one person representing State air pollution control agencies and inserting three persons representing State air pollution control agencies ; and\n**(2)**\nby adding at the end the following: The persons representing State air pollution control agencies shall be from geographically diverse areas with at least one person representing a State located in Region 1, 2, 3, or 5 of the Environmental Protection Agency, one person representing a State located in Region 4, 6, or 7 of the Environmental Protection Agency, and one person representing a State located in Region 8, 9, or 10 of the Environmental Protection Agency. .\n##### (b) Consideration of adverse public health, welfare, social, economic, or energy effects\nSection 109(d)(2) of the Clean Air Act ( 42 U.S.C. 7409(d)(2) ) is amended by adding at the end the following:\n(D) Prior to establishing or revising a national ambient air quality standard, the Administrator shall request, and such committee, after receiving public comments, shall assess and provide advice under subparagraph (C)(iv) regarding any adverse public health, welfare, social, economic, or energy effects which may result from various strategies for attainment and maintenance of such national ambient air quality standard. .",
      "versionDate": "2025-06-27",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-01-16T19:43:58Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-01-16T19:45:51Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2026-01-16T19:44:17Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-16T19:44:29Z"
          },
          {
            "name": "Environmental Protection Agency (EPA)",
            "updateDate": "2026-01-16T19:44:36Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-01-16T19:44:44Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2026-01-16T19:44:10Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-01-16T19:44:54Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-01-16T19:45:00Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-16T19:45:09Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-16T19:45:17Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2026-01-16T19:45:23Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-01-16T19:45:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-07-24T12:59:28Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4218ih.xml"
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
      "title": "CLEAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Air and Economic Advancement Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Clean Air Act to facilitate State implementation of national ambient air quality standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T04:18:27Z"
    }
  ]
}
```
