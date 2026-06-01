# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7057?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7057
- Title: Returning Home Act
- Congress: 119
- Bill type: HR
- Bill number: 7057
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-02-04T19:31:59Z
- Update date including text: 2026-02-04T19:31:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7057",
    "number": "7057",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001300",
        "district": "44",
        "firstName": "Nanette",
        "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
        "lastName": "Barrag\u00e1n",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Returning Home Act",
    "type": "HR",
    "updateDate": "2026-02-04T19:31:59Z",
    "updateDateIncludingText": "2026-02-04T19:31:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-14T15:01:00Z",
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "OR"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "PA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NJ"
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
      "sponsorshipDate": "2026-01-14",
      "state": "DC"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "IL"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "IL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CT"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7057ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7057\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Ms. Barrag\u00e1n (for herself, Mr. Goldman of New York , Mr. Khanna , Ms. Bonamici , Mr. Evans of Pennsylvania , Mrs. Watson Coleman , Ms. Norton , Mrs. Ramirez , Mr. McGovern , Ms. Simon , Mr. Garc\u00eda of Illinois , and Mr. Espaillat ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish the Reentry Rental Assistance and Housing Services Grant Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Returning Home Act .\n#### 2. Reentry Rental Assistance and Housing Services Grant Program\nSection 2976 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10631 ) is amended\u2014\n**(1)**\nin the section heading, by striking offender ;\n**(2)**\nin subsection (a), by striking offender ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin the heading, by striking Offender ;\n**(B)**\nby striking offender ;\n**(C)**\nin paragraph (1)\u2014\n**(i)**\nby striking offenders and inserting individuals ; and\n**(ii)**\nby striking or juvenile facilities and inserting juvenile facilities, or halfway houses ;\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nby striking prison, jail, or a juvenile facility and inserting a prison, jail, juvenile facility, or halfway house ; and\n**(ii)**\nby striking offenders and inserting individuals ;\n**(E)**\nin paragraph (4)(A), by striking offenders and inserting individuals who are incarcerated or who were incarcerated ;\n**(F)**\nin paragraph (5)\u2014\n**(i)**\nby striking or juvenile facility and inserting juvenile facility, or halfway house ; and\n**(ii)**\nby striking offenders while in custody and inserting such individuals during incarceration ;\n**(G)**\nin paragraph (6)\u2014\n**(i)**\nby striking by offenders to victims and inserting by individuals who committed crimes to victims of such crimes ; and\n**(ii)**\nby striking of offenders and inserting of such individuals from a prison, jail, juvenile facility, or halfway house ; and\n**(H)**\nin paragraph (7), by striking dangerous offenders and inserting individuals who are incarcerated and dangerous ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nin the heading, by striking offender ; and\n**(B)**\nby striking offender ;\n**(5)**\nin subsection (d)(2)(A), by striking offender ;\n**(6)**\nin subsection (e)(1), by striking offender ;\n**(7)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1)(B), by striking offender ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking offenders and inserting individuals who are incarcerated ; and\n**(ii)**\nin subparagraph (D), by striking offenders and inserting individuals who are incarcerated ; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking and juvenile facilities and inserting juvenile facilities, and halfway houses ; and\n**(II)**\nby striking offenders and inserting individuals ;\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (ii), by striking offenders and inserting individuals ;\n**(II)**\nin clause (ii), by striking prisons, jails, and juvenile facilities and inserting a prison, jail, juvenile facility, or halfway house ; and\n**(III)**\nin clause (iii), by striking offenders and inserting individuals who are incarcerated or who were incarcerated ;\n**(iii)**\nin subparagraph (C)(ii)\u2014\n**(I)**\nby striking an offender and inserting an incarcerated individual ; and\n**(II)**\nby striking that offenders and inserting that such individuals ;\n**(iv)**\nin subparagraph (F), by striking offenders and inserting individuals who are incarcerated ; and\n**(v)**\nin subparagraph (G)\u2014\n**(I)**\nby striking offenders with histories and inserting individuals who are incarcerated or who were incarcerated and who have a history ; and\n**(II)**\nby striking offender in each place it occurs and inserting individual ;\n**(8)**\nin subsection (h)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking offenders and inserting individuals ; and\n**(ii)**\nby striking prison, jail or a juvenile facility and inserting a prison, jail, juvenile facility, or halfway house ; and\n**(B)**\nin paragraph (4), by striking released offenders and inserting individuals released from a prison, jail, juvenile facility, or halfway house ;\n**(9)**\nin subsection (i)(1)\u2014\n**(A)**\nby striking returning offenders and and inserting individuals reentering the community after time spent in a prison, jail, juvenile facility, or halfway house and to ;\n**(B)**\nby striking offenders' time in prison, jail, or a juvenile facility and inserting such time ;\n**(C)**\nby striking of offenders and inserting of such individuals ; and\n**(D)**\nby striking offender ;\n**(10)**\nin subsection (j)\u2014\n**(A)**\nin paragraph (1), by striking an implementation and inserting a ;\n**(B)**\nin paragraph (2), by striking offenders released back and inserting individuals who were released from a prison, jail, juvenile facility, or halfway house ; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nby striking offenders and inserting individuals ; and\n**(ii)**\nby striking prison, jails, or juvenile facilities and inserting prisons, jails, juvenile facilities, or halfway houses ;\n**(11)**\nin subsection (m)\u2014\n**(A)**\nby striking Juvenile Offender each place such term appears and inserting Juvenile ;\n**(B)**\nin paragraph (2), by striking offender ; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (B), by striking offender ;\n**(ii)**\nin subparagraph (F)\u2014\n**(I)**\nby striking prison, jail, or a juvenile facility and inserting a prison, jail, juvenile facility, or halfway house ; and\n**(II)**\nby striking prisons, jails, or juvenile facilities and inserting a prison, jail, juvenile facility, or halfway house ; and\n**(iii)**\nin subparagraph (I), by striking offenders and inserting individuals who are incarcerated or who were incarcerated ;\n**(12)**\nin subsection (n)(2)(A), by striking offenders and inserting individuals who received assistance from such projects and who are incarcerated or who were incarcerated ;\n**(13)**\nin subsection (o)(2)(B), by striking criminal offenders and inserting individuals who were incarcerated ; and\n**(14)**\nin subsection (p)\u2014\n**(A)**\nby striking offenders reentering the community in each place it occurs and inserting individuals who are reentering the community after incarceration ; and\n**(B)**\nin paragraph (5), by striking offenders and inserting individuals .\n#### 3. Rental assistance and housing grant\nPart FF of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10631 et seq. ) is amended by adding at the end the following:\n2978. Reentry Rental Assistance and Housing Services Grant Program (a) Establishment The Attorney General shall, in coordination with the Secretary of Housing and Urban Development, establish a program to be known as the Reentry Rental Assistance and Housing Services Grant Program to provide grants as provided under this section. (b) Use of funds A grant under this section may be used for\u2014 (1) providing 24 months of rental assistance to an individual who was incarcerated for purposes of paying housing costs at a permanent residence; (2) providing a stipend to a family member of an individual who was incarcerated if the individual lives in the family member\u2019s household; and (3) providing supportive services to individuals who are incarcerated or who were incarcerated, including\u2014 (A) pre-release planning; (B) document collection support; (C) housing counseling and location services; (D) system navigation and linkage support to other services, including mental health therapy, program services for victims of domestic violence, program services for victims of sexual assault, substance abuse treatment, education services, and employment services; (E) information about home-based services and community-based services; (F) case management and addressing criminogenic needs; (G) move-in support and assistance; (H) support with security deposits and other leasing fees; (I) housing placement support; (J) housing stabilization support for at least 12 months to help retain housing after placement; (K) financial incentives to landlords, including payment of holding fees, funds to mitigate property damage, and other incentives to accept tenants who are receiving rental assistance; and (L) other similar supportive services as determined by the Secretary. (c) Allocation for rental assistance A grantee shall use\u2014 (1) not less than 60 percent of the grant funding for rental assistance described under subsection (b)(2); and (2) not more than 15 percent of grant funding for financial incentives to landlords described under subsection (b)(3)(K). (d) Application requirements (1) Application (A) In general An eligible applicant seeking a grant under this section shall submit an application to the Attorney General at such time, in such manner, and containing such information as the Attorney General may require. (B) Eligible applicant For purposes of this paragraph, an eligible applicant is\u2014 (i) an eligible entity; (ii) a nonprofit organization or service provider in partnership with an eligible entity; or (iii) a nonprofit organization or service provider in partnership with\u2014 (I) a collaborative applicant or other entity funded under the Continuum of Care program under subtitle IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11381 et seq. ); (II) a protection and advocacy system (as defined in section 102 of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15002 )); (III) a client assistance program (as described in section 112 of the Rehabilitation Act of 1973 ( 29 U.S.C. 732 )); or (IV) a center for independent living (as defined in section 702 of the Rehabilitation Act of 1973 ( 29 U.S.C. 796a )). (2) Program proposal The Attorney General may make a grant under this section to an applicant only if the applicant submits a proposed program that will benefit\u2014 (A) individuals who are incarcerated in a prison, jail, juvenile facility, or halfway house who are not more than 365 days from their release date and are at risk of becoming homeless or exiting into housing insecurity; (B) individuals experiencing homelessness while under parole or supervised release from a prison, jail, juvenile facility, or halfway house; or (C) individuals experiencing homelessness or housing insecurity and who were discharged from a prison, jail, juvenile facility, or halfway house. (3) Priority considerations The Attorney General shall prioritize grants\u2014 (B) to an applicant that implements a housing first approach which includes low-barrier screening criteria for determining which individuals receive assistance under the program; and (C) to an applicant that implements a program to serve a population that, when compared to the general population, is at a disproportionate risk of incarceration and that experiences a disproportionate rate of homelessness. (4) Prohibition on grants to law enforcement The Attorney General may not provide a grant under this section to a law enforcement entity, including an entity that employs probation officers. (e) Denial notification requirements (1) In general A grantee under this section shall notify individuals who apply for and are denied support from programs funded with such grants about\u2014 (A) the denial; (B) the reason for the denial; and (C) supportive services (including housing counseling) and free legal resources. (2) Timing Such notifications shall be sent to the individual within 15 days after denial. (f) Accessibility requirements A grantee under this section shall ensure that information regarding the programs and support services that the grantee offers and that are funded with such grants is made available\u2014 (1) in a manner that uses simple, plain language and is reader friendly; and (2) in a form that is accessible to individuals with disabilities. (g) Evaluation Not later than 2 years after the date of enactment of this section, the Attorney General shall evaluate the efficacy of the grant awarded under this section in improving outcomes for previously incarcerated individuals. (h) Authorization of appropriations There is authorized to be appropriated $100,000,000 for each fiscal year to carry out this section. (i) Definitions In this section: (1) Disability The term disability has the meaning given to such term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ). (2) Housing costs The term housing costs includes rent, utilities, security deposits, application fees, and other similar expenses as determined by the Attorney General, in consultation with the Secretary. (3) Secretary The term Secretary means the Secretary of Housing and Urban Development. .",
      "versionDate": "2026-01-14",
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
        "updateDate": "2026-02-04T19:31:58Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7057ih.xml"
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
      "title": "Returning Home Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Returning Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish the Reentry Rental Assistance and Housing Services Grant Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T06:48:40Z"
    }
  ]
}
```
