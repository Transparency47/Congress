# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3049
- Title: Tenants’ Right to Organize Act
- Congress: 119
- Bill type: HR
- Bill number: 3049
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2025-12-18T09:06:56Z
- Update date including text: 2025-12-18T09:06:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3049",
    "number": "3049",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Tenants\u2019 Right to Organize Act",
    "type": "HR",
    "updateDate": "2025-12-18T09:06:56Z",
    "updateDateIncludingText": "2025-12-18T09:06:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-28T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MN"
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
      "sponsorshipDate": "2025-05-05",
      "state": "DC"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NJ"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "FL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "IL"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "PA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
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
      "sponsorshipDate": "2025-06-23",
      "state": "MI"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "PA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "VT"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "PA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "FL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MS"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "WA"
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
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3049ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3049\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mrs. Ramirez (for herself, Ms. Tlaib , Mr. Gomez , Mr. Casar , and Ms. Pressley ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the United States Housing Act of 1937 and the Internal Revenue Code to promote the establishment of tenant organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tenants\u2019 Right to Organize Act .\n#### 2. Sense of the Congress\nIt is the sense of the Congress that all members of a household receiving tenant-based rental assistance have the right to decent, safe, stable, and sanitary housing.\n#### 3. Housing choice voucher tenant organizations\nSection 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) is amended by adding at the end the following:\n(23) Right to organize (A) In general A tenant\u2014 (i) has the right to establish, operate, and participate in a legitimate tenant organization for the purpose of addressing issues related to their living environment, which includes\u2014 (I) the terms and conditions of their tenancy; and (II) activities related to housing and community development; (ii) has the right to speak to the public, including media, elected officials, and government agencies with respect to their right to decent, safe, and sanitary housing in compliance with relevant housing codes, fair housing statutes, and any other requirements; and (iii) may not be retaliated against for asserting such rights. (B) Required engagement (i) Public Housing Agencies Each public housing agency shall\u2014 (I) recognize legitimate tenant organizations; (II) give reasonable consideration to concerns raised by legitimate tenant organizations; (III) solicit feedback from any legitimate tenant organization within the public housing agency, including\u2014 (aa) if a public housing agency is required to complete an annual public housing agency plan, feedback with respect to the plan; or (bb) if a public housing agency has an exemption under section 5(b)(3), soliciting feedback not less than once each year; (IV) after receiving feedback from a legitimate tenant organization\u2014 (aa) except as provided in item (bb), meaningfully respond in writing to such comment not later than 60 days after receiving such feedback; and (bb) with respect to exigent poor housing conditions, respond in writing to the feedback not later than 30 days after receiving such feedback; and (V) seek resident advisory board appointments from legitimate tenant organizations. (ii) Owners of units Each owner shall\u2014 (I) recognize legitimate tenant organizations; (II) give reasonable consideration to concerns raised by legitimate tenant organizations; and (III) allow tenant organizers to assist tenants in the establishment and operation of legitimate tenant organizations. (C) Protections (i) In general Each public housing agency and each owner may not\u2014 (I) interfere with the right of any tenant to establish and operate a legitimate tenant organization; and (II) retaliate against any tenant or tenant organizer because of their association with or participation in activities related to a legitimate tenant organization. (ii) Protected activities Each public housing agency, each owner, and agents thereof shall permit tenants and tenant organizers to conduct the following activities related to the establishment or operation of a legitimate tenant organization: (I) Distributing leaflets in lobby areas. (II) Placing leaflets at or under doors of tenants. (III) Distributing leaflets in common areas. (IV) Initiating contact with tenants. (V) Conducting door-to-door surveys of tenants to ascertain interest in establishing a legitimate tenant organization and to offer information about tenant organizations. (VI) Posting information on bulletin boards. (VII) Assisting tenants with participation in tenant organization activities. (VIII) Convening regularly scheduled tenant organization meetings in a space on-site and accessible to tenants, in a manner that is fully independent of representatives of the public housing agency or the owner, unless invited by the tenant organization to specific meetings to discuss a specific issue or issues. (IX) Assisting tenants in\u2014 (aa) creating a resident advisory board or resident council; and (bb) appointing tenants to serve on a resident advisory board or resident council. (X) Speaking to the public, including the media, elected officials, and government agencies. (XI) Formulating a response to a request by the owner or public housing agency for approval of rent increases or other discretionary decisions affecting residents. (XII) Other reasonable activities related to the establishment or operation of a legitimate tenant organization. (iii) Permission A public housing agency or owner may not require tenants or tenant organizers to obtain prior permission before engaging in the activities permitted under this paragraph. (iv) Presumption If a public housing agency or owner takes an adverse action against a tenant or tenant organizer that is a member of a legitimate tenant organization during the 180-day period beginning on the date on which the tenant engages in a protected activity under this subparagraph, there shall be a rebuttable presumption that the adverse action is an act of retaliation relating to the participation of the tenant in the tenant organization. (D) Notice of right to organize Each public housing agency shall notify each tenant of the rights described under this paragraph. (E) Prohibition on interference and retaliation Each public housing agency and each owner may not\u2014 (i) interfere with the right of tenants to establish and operate a legitimate tenant organization; or (ii) retaliate against any tenant or tenant organizer because of their association with or participation in activities related to a legitimate tenant organization. (F) Meeting spaces (i) In general Each public housing agency and owner shall make available the use of any community room or other available space appropriate for meetings within the building or project when requested by a legitimate tenant organization and used for activities related to the establishment or operation of a legitimate tenant organization. (ii) Accessibility If the building or project has an accessible common area or areas, such facilities shall reasonably be made available for legitimate tenant organization meetings to ensure such meetings are accessible to persons with disabilities, unless it is impractical for reasons beyond the control of the public housing agency or owner. (iii) Fees An owner of a building or project may charge a reasonable, customary, and usual fee, as may normally be imposed for the use of such facilities. (G) Definitions In this paragraph: (i) Adverse action The term adverse action means, in response to a tenant\u2019s exercise of rights described in this paragraph\u2014 (I) the termination or non-renewal of a lease; (II) the termination of assistance under this section; (III) a decrease or delay in services provided to the tenant by the owner or public housing agency; (IV) an unplanned increase of rent or fees; (V) the threat or initiation of a lawsuit against a lessee; (VI) a violation of tenant privacy; or (VII) the harassment of a tenant or tenant organizers. (ii) Legitimate tenant organization The term legitimate tenant organization means, in a building or project with 3 or more families receiving assistance under this section, an organization that\u2014 (I) meets regularly and operates democratically; (II) is representative of all tenants in the building or project; (III) is completely independent from a public housing agency, owner, landlord, management of the building or development, and any representatives of such entities; (IV) has been established for the purpose described in subparagraph (A); and (V) includes newly formed resident organizing committees, which do not require specific structures, written by-laws, elections, or resident petitions. (iii) Tenant The term tenant means a family or any member of a family that receives assistance under this section. (iv) Tenant organizer (I) In general The term tenant organizer means an individual who\u2014 (aa) assists tenants in establishing and operating a legitimate tenant organization; and (bb) is not an employee or representative of current or prospective owners or agents or the owners. (II) Building policies (aa) Policy against canvassing If a building or project has consistently enforced a written policy against canvassing, any tenant organizer who is not a tenant shall be accompanied by a tenant while on the property of the building or project. (bb) Policy in favor of canvassing If a building or project has a written policy favoring canvassing, any tenant organizer who is not a tenant shall be afforded the same privileges and rights of access as any other uninvited outside parties in the normal course of operations of the building or project. (cc) No policy on canvassing If a building or project does not have a consistently enforced, written policy against canvassing, the building or project shall be treated as if it has a policy favoring canvassing. .\n#### 4. LIHTC tenant organizations\n##### (a) In general\nSection 42(g) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(10) LIHTC tenant organizations (A) Rights of tenants In the case of any qualified low-income housing project which is an applicable project, families occupying rent-restricted units in such project shall have the same right as families described in section 8(o)(23)(B)(i), (ii) and (iii) of the United States Housing Act of 1937. (B) Responsibilities of owners and state housing credit agencies In the case of any applicable project, such project shall not be treated as a qualified low-income housing project for purposes of this section unless\u2014 (i) each owner of such project meets requirements which are the same as the requirements of clauses (i) and (iii) of subparagraph (C) and subparagraph (D) of section 8(o)(23) of the United States Housing Act of 1937, and (ii) each State housing credit agency meets requirements which are the same as the requirements of clauses (i) and (ii) of subparagraph (C) and subparagraph (D) of such section. (C) Applicable project For purposes of this paragraph, the term applicable project means\u2014 (i) any project which is placed in service after the date of enactment of this Act; and (ii) any project\u2014 (I) which was placed in service on or before the date of enactment of such Act; and (II) for which the date of enactment of such Act occurred before the end of the compliance period for such project. (D) Notice of right to organize (i) In general Each State housing credit agency shall notify each tenant living at a qualified low-income housing project of the right to organize as described in paragraph (10) annually. (ii) Tenancy addendum The Secretary shall require each State housing credit agency\u2014 (I) that has implemented a standard lease, lease addendum, or other guidance to owners of a qualified low-income housing project, to amend that document to include language affirming lessees\u2019 right to organize provided for in this paragraph; or (II) that performs lease-based evaluations of low income-housing tax credit compliance to include in that evaluation a requirement to include a written affirmation of the tenant\u2019s right to organize as provided for in this paragraph. (E) Authorization of appropriations There are authorized to be appropriated to the Secretary such sums as are necessary to carry out this paragraph. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 5. Enforcement\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Assistant Secretary for Public and Indian Housing of the Department of Housing and Urban Development shall, in coordination with the Secretary of the Treasury, establish a protocol for the enforcement of paragraph (23) of section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(23) ), as added by section 3 of this Act, and paragraph (10) of section 42(g) of the Internal Revenue Code of 1986, as added by section 4 of this Act, that\u2014\n**(1)**\nreflects or integrates the existing enforcement protocol for tenants protected under section 202 of the Housing and Community Development Amendments Act of 1978 ( 12 U.S.C. 1715z\u20131b ), where possible;\n**(2)**\ncreates a mechanism for administrative complaints to be filed, cataloged, and investigated regarding public housing agencies, State housing credit agencies, owners, landlords, management, and their representatives\u2019 alleged violation of their obligation not to interfere with the right of tenants to establish and operate a legitimate tenant organization, which shall\u2014\n**(A)**\nprovide families a remedy when the agency determines a violation of the obligation not to interfere with the right of tenants to establish and operate a legitimate tenant organization;\n**(B)**\ninclude an independent investigation of tenant and advocate allegations of abuse;\n**(C)**\nkeep tenants informed about the progression of any complaint; and\n**(D)**\nprovide confidentiality if necessary, including in cases where alleged abuse is extreme and targeted;\n**(3)**\nprohibits withholding the tenant-based assistance under such section 8(o) or the denial of the right to occupy an assisted unit or a rent-restricted unit, or any other right or privilege required to be provided as a condition of the tenant-based assistance or the project being treated as a qualified low-income housing project until such complaint is closed; and\n**(4)**\nif relevant, appropriately refers complaints related to potential violation of fair housing laws to the Office of Fair Housing and Equal Opportunity at the Department of Housing and Urban Development.\n##### (b) Establishment of private right of action\nTenants may file an action at law or in equity, in Federal or State court, including for injunctive relief, to enforce the various provisions of this Act.\n##### (c) Report\nThe Secretary of Housing and Urban Development shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a quarterly report on the enforcement of this section that\u2014\n**(1)**\nprovides all data at both the property-level and jurisdiction-level; and\n**(2)**\nincludes\u2014\n**(A)**\nthe volume of outstanding complaints;\n**(B)**\nthe average response time to an initial complaint;\n**(C)**\nthe average time it takes to close a complaint; and\n**(D)**\ninformation about the type of issues reported by tenants that necessitated enforcement action.\n#### 6. Funding for tenant and other participation and capacity building\nParagraph (3) of section 514(f) of the Multifamily Assisted Housing Reform and Affordability Act of 1997 ( 42 U.S.C. 1437f note) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin the first sentence\u2014\n**(i)**\nby striking not more than and inserting not less than ;\n**(ii)**\nby inserting for predevelopment assistance to enable such transfers, after owners), ; and\n**(iii)**\nby striking of low-income housing for which project-based rental assistance is provided at below market rent levels and may not be renewed (including transfer of developments to tenant groups, nonprofit organizations, and public entities), for tenant services and inserting the following: and improvement of low-income housing for which project-based rental assistance, public housing subsidies, low-income housing tax credits, Federal or State subsidized loans, enhanced vouchers under section 8(t) of the United States Housing Act of 1937, or project-based vouchers under section 8(o) of such Act are provided or proposed ; and\n**(B)**\nby adding at the end the following:\n(D) Outreach and technical assistance grants (i) In general Not later than 1 year after the date of the enactment of this subparagraph, the Secretary shall establish a grant program to award amounts for the purposes of, under this paragraph\u2014 (I) outreach and training of tenants by eligible entities; and (II) the provision of technical assistance by eligible entities to tenant groups. (ii) Eligible entities To be eligible for a grant under this subparagraph, an entity shall be a nonprofit organization that\u2014 (I) has not less than 2 years of experience with the organization and provision of assistance to tenants; and (II) is independent from any owners, prospective purchasers, or any agents thereof of a residential development. (iii) Assistance to eligible entities The Secretary may provide assistance and training to recipients of amounts under subparagraph with respect to\u2014 (I) administrative and fiscal management; and (II) compliance with any Federal requirements. (iv) Expedited funding The Secretary shall expedite the provision of funding for the fiscal year in which the date of the enactment of this subparagraph occurs by entering into an interagency agreement for not less than $1,000,000 with the Corporation for National and Community Service to conduct a tenant outreach and training program. (v) Flexible grants The Secretary shall make available flexible grants under this subparagraph to qualified nonprofit organizations that do not own eligible multifamily properties, for tenant outreach in underserved areas, and to experienced national or regional nonprofit organizations to provide specialized training or support to grantees assisted under this subsection. (vi) Funding for subsequent fiscal years Notwithstanding any other provision of law, amounts authorized under this subparagraph for any fiscal year shall be available for obligation in subsequent fiscal years. (vii) Reports The Secretary shall require each recipient of amounts made available pursuant to this subparagraph to submit to the Secretary a report, on a quarterly basis, detailing the use of such amounts, including such information as the Secretary shall require. .\n#### 7. Provision of funds to resident councils\nThe Secretary of Housing and Urban Development shall, not later than 1 year after the date of the enactment of this Act, provide each resident council, as described in section 964.100 of title 24, Code of Federal Regulations, $40 per unit per year, to be increased annually to keep pace with inflation.",
      "versionDate": "2025-04-28",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-05-21T14:06:07Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3049ih.xml"
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
      "title": "Tenants\u2019 Right to Organize Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:14:08Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tenants\u2019 Right to Organize Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the United States Housing Act of 1937 and the Internal Revenue Code to promote the establishment of tenant organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:51Z"
    }
  ]
}
```
