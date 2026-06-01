# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6845?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6845
- Title: S.T.O.P. Illicit Vapes Act
- Congress: 119
- Bill type: HR
- Bill number: 6845
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-21T08:08:07Z
- Update date including text: 2026-05-21T08:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6845",
    "number": "6845",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001136",
        "district": "3",
        "firstName": "Herbert",
        "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
        "lastName": "Conaway",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "S.T.O.P. Illicit Vapes Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:07Z",
    "updateDateIncludingText": "2026-05-21T08:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-18T14:03:10Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "DC"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "UT"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "AZ"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NY"
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
      "sponsorshipDate": "2026-05-19",
      "state": "VA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6845ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6845\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Conaway (for himself, Ms. Norton , Mr. Krishnamoorthi , and Ms. Maloy ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a Federal multi-agency task force to combat illegal importation, distribution, and sale of e-cigarettes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Task Force Operations to Prevent Illicit Vapes Act or the S.T.O.P. Illicit Vapes Act .\n#### 2. Federal multi-agency task force to combat illegal importation, distribution, and sale of e-cigarettes\n##### (a) Establishment\nOn the date that is 30 days after the date of enactment of this Act, there shall be established (or reestablished) a multi-agency task force to combat the illegal importation, distribution, and sale of e-cigarettes (in this section referred to as the Task Force ).\n##### (b) Purpose\nThe Task Force shall develop and implement a comprehensive strategy for reducing the number of unauthorized e-cigarettes in the market, including setting goals, sharing information, and coordinating efforts where appropriate.\n##### (c) Membership\nThe Task Force shall be composed of each of the following members:\n**(1)**\nThe Attorney General, who shall serve as co-chair.\n**(2)**\nThe Secretary of Health and Human Services, who shall serve as co-chair.\n**(3)**\nAt least one representative of the Food and Drug Administration, appointed by the Commissioner of Food and Drugs.\n**(4)**\nAt least one representative of the Department of Justice, appointed by the Attorney General.\n**(5)**\nA representative of U.S. Customs and Border Protection, appointed by the Commissioner of U.S. Customs and Border Protection.\n**(6)**\nA representative of the Bureau of Alcohol, Tobacco, Firearms and Explosives, appointed by the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives.\n**(7)**\nA representative of the United States Marshals Service, appointed by the Director of the United States Marshals Service.\n**(8)**\nA representative of the United States Postal Inspection Service, appointed by the Chief Postal Inspector.\n**(9)**\nA representative of the Federal Trade Commission, appointed by the Chair of the Federal Trade Commission.\n**(10)**\nA representative of Homeland Security Investigations, appointed by the Executive Associate Director of Homeland Security Investigations.\n**(11)**\nA representative of the Federal Bureau of Investigation, appointed by the Director of the Federal Bureau of Investigation.\n**(12)**\nRepresentatives of such other Federal agencies that have roles or responsibilities related to e-cigarette enforcement, as appointed by the co-chairs of the Task Force, acting jointly.\n##### (d) Meetings\nThe Task Force shall meet not less frequently than once every 30 days.\n##### (e) Semiannual reports\n**(1) In general**\nNot later than April 30 and October 31 of each year, the Task Force shall submit to the appropriate congressional committees a report detailing\u2014\n**(A)**\nthe authorities of each agency represented on the Task Force to combat the illegal importation, distribution, and sale of e-cigarettes;\n**(B)**\nall actions taken by each agency represented on the Task Force to combat the illegal importation, distribution, and sale of e-cigarettes, including the investigation and prosecution of criminal, civil, seizure, and forfeiture actions, including enforcement actions against unauthorized e-cigarette manufacturers, importers, and distributors, during the 6-month period\u2014\n**(i)**\nwith respect to a report due on April 30, ending on the immediately preceding March 31; or\n**(ii)**\nwith respect to a report due on October 31, ending on the immediately preceding September 30;\n**(C)**\nrecommendations for additional criminal or civil authorities that may be necessary to address the public health threat of the illegal importation, distribution, and sale of e-cigarettes; and\n**(D)**\nareas for improvement with respect to collaboration among the agencies represented on the Task Force.\n**(2) Appropriate congressional committees**\nIn this subsection, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on the Judiciary, the Committee on Health, Education, Labor, and Pensions, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on the Judiciary, the Committee on Energy and Commerce, and the Committee on Appropriations of the House of Representatives.\n##### (f) Sunset\nThe Task Force shall terminate on the date that is 10 years after the date on which the Task Force is established under subsection (a).",
      "versionDate": "2025-12-18",
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
        "actionDate": "2025-12-18",
        "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S8924)"
      },
      "number": "3569",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "S.T.O.P. Illicit Vapes Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-22T15:10:55Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6845ih.xml"
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
      "title": "S.T.O.P. Illicit Vapes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "S.T.O.P. Illicit Vapes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Task Force Operations to Prevent Illicit Vapes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Federal multi-agency task force to combat illegal importation, distribution, and sale of e-cigarettes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:33Z"
    }
  ]
}
```
