# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5085?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5085
- Title: To exempt Federal actions related to the construction of infill housing from the requirements of the National Environmental Policy Act of 1969, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5085
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2026-01-21T09:05:26Z
- Update date including text: 2026-01-21T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-03 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-02 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-03 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5085",
    "number": "5085",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "F000483",
        "district": "30",
        "firstName": "Laura",
        "fullName": "Rep. Friedman, Laura [D-CA-30]",
        "lastName": "Friedman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To exempt Federal actions related to the construction of infill housing from the requirements of the National Environmental Policy Act of 1969, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:26Z",
    "updateDateIncludingText": "2026-01-21T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-03T21:38:01Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-02T16:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NC"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "RI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "KS"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PR"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5085ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5085\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Ms. Friedman (for herself, Mr. Edwards , Mr. Peters , and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo exempt Federal actions related to the construction of infill housing from the requirements of the National Environmental Policy Act of 1969, and for other purposes.\n#### 1. Exemption of Federal actions related to the construction of infill housing from the requirements of the National Environmental Policy Act of 1969\n##### (a) Exemption\nAn action by a Federal agency related to an infill housing activity may not be considered a major Federal action under section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ).\n##### (b) Definitions\nIn this section:\n**(1) Hazardous substance; pollutant or contaminant; release; remedial action**\nThe terms hazardous substance , pollutant or contaminant , release , and remedial action have the meanings given such terms, respectively, in section 101 of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9601 ).\n**(2) Infill housing**\nThe term Infill housing means residential housing\u2014\n**(A)**\nthat is located on a site\u2014\n**(i)**\nthat is vacant or underutilized;\n**(ii)**\nthat has been previously developed with an urban use;\n**(iii)**\nthat is not larger than 20 acres;\n**(iv)**\n**(I)**\nat least 75 percent of the perimeter of which adjoins a parcel that was developed with an urban use; or\n**(II)**\nat least 75 percent of the area within a 1/4-mile from the exterior boundary of which is developed with an urban use; and\n**(v)**\nthat has undergone a Phase I Environmental Site Assessment in accordance with the applicable industry standards described in section 312.11 of title 40, Code of Federal Regulations, (or any successor regulation) and, if the Phase I Environmental Site Assessment identified conditions indicative of a release or threatened release of a hazardous substance, a pollutant or contaminant, petroleum, or a petroleum product, the site has undergone a Phase II Environmental Site Assessment in accordance with ASTM E1903\u201319 (as in effect on the date of enactment of this section) that\u2014\n**(I)**\ndid not show a release of a hazardous substance, a pollutant or contaminant, petroleum, or a petroleum product; or\n**(II)**\nshows a release of a hazardous substance, pollutant or contaminant, petroleum, or a petroleum product, but the site has been remediated to the standard applicable to a remedial action under the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9601 et seq. ); and\n**(B)**\nthat is not located on a site within a census tract designated as very high or relatively high risk for wildfire, coastal flooding, and riverine flooding under the National Risk Index of the Federal Emergency Management Agency pursuant to section 206 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5136 ).\n**(3) Infill housing activity**\nThe term infill housing activity means\u2014\n**(A)**\nthe acquisition or disposition of land or property for the development of infill housing;\n**(B)**\nthe demolition of property (not including a historic structure designated on a national, State, or local historic register) for the construction, reconstruction, rehabilitation, or development of infill housing;\n**(C)**\nthe construction, reconstruction, rehabilitation, or development of infill housing; or\n**(D)**\nthe conversion of a non-residential building into infill housing.\n**(4) Urban use**\nThe term urban use means any residential use, commercial use, industrial use, public institutional use, transit or transportation passenger facility use, retail use, or any combination of such uses.\n#### 2. Natural hazard risk assessment updates\nSection 206(d)(1) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5136(d)(1) ) is amended by striking every 5 years and inserting every 3 years .",
      "versionDate": "2025-09-02",
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
        "name": "Emergency Management",
        "updateDate": "2025-09-17T20:04:17Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5085ih.xml"
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
      "title": "To exempt Federal actions related to the construction of infill housing from the requirements of the National Environmental Policy Act of 1969, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:28Z"
    },
    {
      "title": "To exempt Federal actions related to the construction of infill housing from the requirements of the National Environmental Policy Act of 1969, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T08:05:19Z"
    }
  ]
}
```
