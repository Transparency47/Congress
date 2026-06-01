# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4755?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4755
- Title: LEO K9 Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 4755
- Origin chamber: House
- Introduced date: 2025-07-25
- Update date: 2026-01-09T09:06:45Z
- Update date including text: 2026-01-09T09:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-25: Introduced in House
- 2025-07-21 - IntroReferral: Sponsor introductory remarks on measure. (CR H3481)
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-21: Sponsor introductory remarks on measure. (CR H3481)

## Actions

- 2025-07-21 - IntroReferral: Sponsor introductory remarks on measure. (CR H3481)
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Introduced in House
- 2025-07-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-25 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-25",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Sponsor introductory remarks on measure. (CR H3481)"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4755",
    "number": "4755",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "LEO K9 Protection Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:45Z",
    "updateDateIncludingText": "2026-01-09T09:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-25",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-25",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3481)",
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
          "date": "2025-07-25T15:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-25T15:03:25Z",
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
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4755ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4755\nIN THE HOUSE OF REPRESENTATIVES\nJuly 25, 2025 Mr. Bean of Florida (for himself and Mr. Mills ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 18, United States Code, to prohibit harming animals used in law enforcement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the LEO K9 Protection Act .\n#### 2. Harming animals used in law enforcement\nSection 1368 of title 18, United States Code, is amended by striking subsection (b) and inserting the following:\n(b) Whoever, in the commission of any act described in subsection (a), uses a deadly or dangerous weapon (including a weapon intended to cause death or danger but that fails to do so by reason of a defective component), shall be fined under this title or imprisoned not more than 15 years, or both. (c) In this section, the term police animal means a dog or horse in the service of a Federal agency (whether in the executive, legislative, or judicial branch), or in the service of a State, county, or local agency that is assisting a Federal agency\u2014 (1) for the principal purpose of aiding in the detection of criminal activity, enforcement of laws, or the apprehension of criminal offenders, the detection of flammable materials, the investigation of fires, the detection of missing persons (including persons who are lost, who are trapped under debris as the result of a natural, manmade, or technological disaster, or who are drowning victims); or (2) used in any official military capacity by the Department of Defense. (d) This section does not apply to a person who acts in good faith to provide emergency veterinary care to an injured police animal. .\n#### 3. Medical transportation for police dogs injured in official duty\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation, acting through the Office of Emergency Medical Services Initiatives at the National Highway Transportation Safety Administration, shall publish guidance for emergency medical services personnel in order to care for police dogs injured while such police dog is engaged in official duties of the dog. The Secretary shall develop such guidance using existing Federal guidelines of the Department of Homeland Security, the Department of Defense, the Canine Tactical Combat Casualty Care Guidelines, and other resources already available at Federal agencies. The Secretary may consult accredited veterinarians, as necessary, in developing the guidance under this section.\n#### 4. Regulations for Emergency Medical Transportation Services\nNot later than 240 days after the date of enactment of this Act, the Secretary of Transportation shall promulgate regulations to ensure that\u2014\n**(1)**\na police dog injured while such police dog is engaged in official duties of the dog may be transported to a veterinary clinic or similar facility if there is no individual requiring medical attention or transport at that time; and\n**(2)**\na paramedic or an emergency medical technician may provide emergency medical care to a police dog while such police dog is engaged in official duties of the dog while at the scene of the emergency or while the police dog is being transported to a veterinary clinic or similar facility.\n#### 5. Definition\nIn this Act, the term police dog means a police animal (as such term is defined in section 1368 of title 18, United States Code) that is a dog, and includes a similar dog working in the service of a State, county, or local agency.",
      "versionDate": "2025-07-25",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-12T18:23:51Z"
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
      "date": "2025-07-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4755ih.xml"
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
      "title": "LEO K9 Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LEO K9 Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit harming animals used in law enforcement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:18Z"
    }
  ]
}
```
