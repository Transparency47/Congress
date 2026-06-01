# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5286?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5286
- Title: Humane Transport of Farmed Animals Act
- Congress: 119
- Bill type: HR
- Bill number: 5286
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-05-16T08:07:09Z
- Update date including text: 2026-05-16T08:07:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-10 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5286",
    "number": "5286",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Humane Transport of Farmed Animals Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:09Z",
    "updateDateIncludingText": "2026-05-16T08:07:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:55:48Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-10T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "MP"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "DC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "TN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MI"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5286ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5286\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Ms. Titus (for herself, Ms. King-Hinds , Ms. Norton , Mr. Cohen , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 49, United States Code, to direct the Secretary of Transportation to develop an enforcement mechanism with respect to certain provisions relating to the transport of animals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Humane Transport of Farmed Animals Act .\n#### 2. Transport of animals\nSection 80502 of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (f); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Enforcement Not later than 180 days after the date of enactment of this subsection, the Secretary of Transportation, in consultation with the Secretary of Agriculture, shall develop a mechanism for conducting investigations or inspections, including the inspection of any vehicle or vessel transporting animals or any written or electronic records associated with such transport of animals, to determine whether any rail carrier, express carrier, or common carrier, a receiver, trustee, or lessee of one of such carriers, or an owner or master of a vessel transporting animals has violated or is violating this section. (e) Additional authority To carry out subsection (d), the Secretary of Transportation and the Secretary of Agriculture shall promulgate such rules and regulations, and issue such orders or guidance, as are necessary. .\n#### 3. Prohibition on interstate movement of certain animals\nSection 10406 of the Animal Health Protection Act ( 7 U.S.C. 8305 ) is amended\u2014\n**(1)**\nby striking The Secretary may prohibit and inserting the following:\n(a) In general The Secretary may prohibit ; and\n**(2)**\nby adding at the end the following:\n(b) Prohibition (1) In general No person shall move in interstate commerce livestock that are unfit to travel. (2) Unfit defined (A) In general For purposes of paragraph (1), the term unfit to travel means, with respect to the movement of livestock, that such livestock are deemed unfit to travel pursuant to Article 7.3.7(3), Chapter 7.3 of the World Organisation for Animal Health\u2019s Terrestrial Animal Health Code, including successive changes. (B) Inclusions Such term includes livestock that\u2014 (i) are sick, injured, weak, disabled, or fatigued; (ii) are unable to stand unaided or bear weight on each leg; (iii) are blind in both eyes; (iv) cannot be moved without causing additional suffering; (v) are newborn with a navel that has not been fully healed; (vi) are pregnant and that would be in the final 10 percent of their gestation period at the planned time of unloading; (vii) have given birth within the previous 48 hours and are traveling without their offspring; or (viii) have a body condition that would result in poor welfare because of the expected climatic conditions. (3) Exception Nothing in this subsection shall be construed to limit the movement in interstate commerce of any livestock for purposes of providing veterinary care to such livestock. .",
      "versionDate": "2025-09-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-24T14:13:59Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5286ih.xml"
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
      "title": "Humane Transport of Farmed Animals Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Humane Transport of Farmed Animals Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to direct the Secretary of Transportation to develop an enforcement mechanism with respect to certain provisions relating to the transport of animals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:19Z"
    }
  ]
}
```
