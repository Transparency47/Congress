# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5098
- Title: Strengthening Our Workforce Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5098
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2025-09-22T15:37:57Z
- Update date including text: 2025-09-22T15:37:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5098",
    "number": "5098",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Strengthening Our Workforce Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-22T15:37:57Z",
    "updateDateIncludingText": "2025-09-22T15:37:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "text": "Referred to the House Committee on the Judiciary.",
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
          "date": "2025-09-02T16:01:45Z",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MN"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5098ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5098\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Mr. Vasquez (for himself, Ms. Craig , Mr. Vargas , Mrs. Ramirez , and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for conditional lawful permanent residency for certain aliens.\n#### 1. Short title\nThis Act may be cited as the Strengthening Our Workforce Act of 2025 .\n#### 2. Conditional lawful permanent residency\n##### (a) In general\nThe Secretary may adjust the status of an alien to that of a conditional lawful permanent resident in accordance with this section.\n##### (b) Status defined\nFor purposes of this section, the term conditional lawful permanent resident means a status as a nonimmigrant with a period of stay of 2 years, with employment authorization to be provided concurrently.\n##### (c) Eligibility\nAn alien is eligible for adjustment of status if that alien\u2014\n**(1)**\nsubmits an application, at such time, in such form, and containing such information as the Secretary may require;\n**(2)**\npays such fee as the Secretary may establish;\n**(3)**\nis present in the United States as of January 1, 2024\u2014\n**(A)**\nwithout lawful status under the immigration laws;\n**(B)**\nwith deferred action granted to the alien pursuant to the Deferred Action for Childhood Arrivals program announced by President Obama on June 15, 2012; or\n**(C)**\nwith status as a nonimmigrant that has employment authorization;\n**(4)**\nhas been continuously present in the United States during the period beginning on January 1, 2024, through the date of the application for status;\n**(5)**\nhas been employed for a cumulative period of one hundred days (consecutive or not) at any time, in a covered profession; and\n**(6)**\nis not inadmissible under paragraph (1), (6)(E), (6)(G), (8), or (10) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ), except that with respect to any benefit under this Act, and in addition to the waivers under subsection (g), the Secretary may waive the grounds of inadmissibility under paragraph (1), (6)(E), (6)(G), or (10)(D) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) for humanitarian purposes, for family unity, or because the waiver is otherwise in the public interest;\n##### (d) Conditions of status\nAn alien granted conditional lawful permanent resident status under this section shall conform to the following requirements:\n**(1)**\nThe alien shall remain continuously physically present in the United States.\n**(2)**\nThe alien shall maintain not less than one hundred cumulative days of annual employment for two consecutive years in a covered profession.\n**(3)**\nThe alien shall be subject to all grounds of deportability under section 237.\n##### (e) Adjustment of status\nAt the time that the conditional lawful permanent resident status of an alien terminates, the Secretary shall immediately adjust the status of that alien to that of a lawful permanent resident\u2014\n**(1)**\nunless the alien makes a timely objection in writing; and\n**(2)**\nif the alien pays such fee as the Secretary may establish and passes an additional background investigation.\n##### (f) Not subject to numerical limitations\nAn alien whose status is adjusted to that of an alien lawfully admitted for permanent residency under this section is not subject to the worldwide levels or numerical limitations of section 201(a) of the Immigration and Nationality Act.\n##### (g) Criminal and national security bars\n**(1) Grounds of ineligibility**\nExcept as provided in paragraph (2), an alien is ineligible for adjustment of status under this title if any of the following apply:\n**(A)**\nThe alien is inadmissible under paragraph (2) or (3) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ).\n**(B)**\nExcluding any offense under State law for which an essential element is the alien\u2019s immigration status, and any minor traffic offense, the alien has been convicted of\u2014\n**(i)**\nany felony offense;\n**(ii)**\nthree or more misdemeanor offenses (excluding simple possession of cannabis or cannabis-related paraphernalia, any offense involving cannabis or cannabis-related paraphernalia which is no longer prosecutable in the State in which the conviction was entered, and any offense involving civil disobedience without violence) not occurring on the same date, and not arising out of the same act, omission, or scheme of misconduct; or\n**(iii)**\na misdemeanor offense of domestic violence, unless the alien demonstrates that such crime is related to the alien having been\u2014\n**(I)**\na victim of domestic violence, sexual assault, stalking, child abuse or neglect, abuse or neglect in later life, or human trafficking;\n**(II)**\nbattered or subjected to extreme cruelty; or\n**(III)**\na victim of criminal activity described in section 101(a)(15)(U)(iii) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(U)(iii) ).\n**(2) Waivers for certain misdemeanors**\nFor humanitarian purposes, family unity, or if otherwise in the public interest, the Secretary may\u2014\n**(A)**\nwaive the grounds of inadmissibility under subparagraphs (A), (C), and (D) of section 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ), unless the conviction forming the basis for inadmissibility would otherwise render the alien ineligible under paragraph (1)(B) (subject to subparagraph (B)); and\n**(B)**\nfor purposes of clauses (ii) and (iii) of paragraph (1)(B), waive consideration of\u2014\n**(i)**\none misdemeanor offense if the alien has not been convicted of any offense in the 5-year period preceding the date on which the alien applies for adjustment of status under this title; or\n**(ii)**\nup to two misdemeanor offenses if the alien has not been convicted of any offense in the 10-year period preceding the date on which the alien applies for adjustment of status under this title.\n**(3) Definitions**\nFor purposes of this subsection\u2014\n**(A)**\nthe term felony offense means an offense under Federal or State law that is punishable by a maximum term of imprisonment of more than 1 year;\n**(B)**\nthe term misdemeanor offense means an offense under Federal or State law that is punishable by a term of imprisonment of more than 5 days but not more than 1 year; and\n**(C)**\nthe term crime of domestic violence means any offense that has as an element the use, attempted use, or threatened use of physical force against a person committed by a current or former spouse of the person, by an individual with whom the person shares a child in common, by an individual who is cohabiting with or has cohabited with the person as a spouse, by an individual similarly situated to a spouse of the person under the domestic or family violence laws of the jurisdiction where the offense occurs, or by any other individual against a person who is protected from that individual\u2019s acts under the domestic or family violence laws of the United States or any State, Indian Tribal government, or unit of local government.\n##### (h) Definitions\nFor purposes of this section:\n**(1) In general**\nTerms used have the meanings given such terms in section 101 of the Immigration and Nationality Act.\n**(2) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n**(3) Covered profession defined**\nFor purposes of this section, the term covered profession means the following:\n**(A)**\nHealth care.\n**(B)**\nEmergency response.\n**(C)**\nEnergy.\n**(D)**\nEducation, including early education.\n**(E)**\nSanitation.\n**(F)**\nRestaurant ownership, food preparation, vending, catering, food packaging, food services, or delivery.\n**(G)**\nHotel or retail.\n**(H)**\nFish, poultry, and meat processing work.\n**(I)**\nAgricultural work, including labor that is seasonal in nature.\n**(J)**\nCommercial or residential landscaping.\n**(K)**\nCommercial or residential construction or renovation.\n**(L)**\nHousing, residential, and commercial construction related activities or public works construction.\n**(M)**\nDomestic work in private households, including child care, home care, or house cleaning.\n**(N)**\nNatural disaster recovery, disaster reconstruction, and related construction.\n**(O)**\nHome and community-based work, including\u2014\n**(i)**\nhome health care;\n**(ii)**\nresidential care;\n**(iii)**\nassistance with activities of daily living;\n**(iv)**\nany service provided by direct care workers (as defined in section 799B of the Public Health Service Act ( 42 U.S.C. 295p )), personal care aides, job coaches, or supported employment providers; and\n**(v)**\nany other provision of care to individuals in their homes by direct service providers, personal care attendants, and home health aides.\n**(P)**\nFamily care, including child care services, in-home child care services such as nanny services, and care services provided by family members to other family members.\n**(Q)**\nManufacturing.\n**(R)**\nWarehousing.\n**(S)**\nTransportation or logistics.\n**(T)**\nJanitorial.\n**(U)**\nLaundromat and dry-cleaning operators.\n**(V)**\nAny other work performed by essential critical infrastructure workers , as described in the memorandum of the Department of Homeland Security entitled Advisory Memorandum on Ensuring Essential Critical Infrastructure Workers Ability to Work During the COVID\u201319 Response , which was originally issued by the Director of the Cybersecurity and Infrastructure Security Agency on March 19, 2020, and last updated on August 10, 2021.\n**(W)**\nAny other work, industry, or profession that a State or local government deemed essential during the COVID\u201319 Public Health Emergency.\n**(X)**\nWorkers who are employed in any of the listed professions who do so remotely or hybrid.",
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
        "name": "Immigration",
        "updateDate": "2025-09-22T15:37:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5098ih.xml"
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
      "title": "To provide for conditional lawful permanent residency for certain aliens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:29Z"
    },
    {
      "title": "Strengthening Our Workforce Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-06T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Our Workforce Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:23:21Z"
    }
  ]
}
```
