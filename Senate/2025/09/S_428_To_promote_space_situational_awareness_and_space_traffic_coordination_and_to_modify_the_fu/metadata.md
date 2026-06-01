# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/428
- Title: SAFE Orbit Act
- Congress: 119
- Bill type: S
- Bill number: 428
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2026-02-04T05:06:13Z
- Update date including text: 2026-02-04T05:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-65.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-65.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 170.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-65.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-65.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 170.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/428",
    "number": "428",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SAFE Orbit Act",
    "type": "S",
    "updateDate": "2026-02-04T05:06:13Z",
    "updateDateIncludingText": "2026-02-04T05:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 170.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-65.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-65.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-09-29T19:33:33Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-05T21:22:38Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "MS"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "TN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "AZ"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "MO"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s428is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 428\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Cornyn (for himself, Mr. Peters , Mr. Wicker , Mrs. Blackburn , Mr. Hickenlooper , Mr. Kelly , Mr. Schmitt , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo promote space situational awareness and space traffic coordination and to modify the functions and leadership of the Office of Space Commerce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Situational Awareness of Flying Elements in Orbit Act or the SAFE Orbit Act .\n#### 2. Space situational awareness and space traffic coordination\n##### (a) In general\nThe Secretary of Commerce shall facilitate safe operations in space and encourage the development of commercial space capabilities by acquiring and disseminating unclassified data, analytics, information, and services on space activities.\n##### (b) Immunity\nThe United States, any agencies and instrumentalities thereof, and any individuals, firms, corporations, and other persons acting for the United States Government, including nongovernmental entities, shall be immune from any suit in any court for any cause of action arising from the provision or receipt of space situational awareness services or information, whether or not provided in accordance with this section, or any related action or omission.\n##### (c) Acquisition of data\nThe Assistant Secretary of Commerce for Space Commerce (established under section 50702(b) of title 51, United States Code, as amended by section 3) is authorized to acquire\u2014\n**(1)**\ndata, analytics, information, and services, including with respect to\u2014\n**(A)**\nlocation tracking data;\n**(B)**\npositional and orbit determination information; and\n**(C)**\nconjunction data messages; and\n**(2)**\nsuch other data, analytics, information, and services as the Secretary of Commerce determines necessary to avoid collisions of space objects.\n##### (d) Database on satellite location and behavior\nThe Assistant Secretary of Commerce for Space Commerce shall provide access for the public, at no charge, a fully updated, unclassified database of information concerning space objects and behavior that includes\u2014\n**(1)**\nthe data and information acquired under subsection (c), except to the extent that such data or information is classified or a trade secret (as defined in section 1839 of title 18, United States Code); and\n**(2)**\nthe provision of basic space situational awareness services and space traffic coordination based on the data referred to in paragraph (1), including basic analytics, tracking calculations, and conjunction data messages.\n##### (e) Basic space situational awareness services\nThe Assistant Secretary of Commerce for Space Commerce\u2014\n**(1)**\nshall provide to satellite operators, at no charge, basic space situational awareness services, including the data, analytics, information, and services described in subsection (c);\n**(2)**\nin carrying out paragraph (1), may not compete with private sector space situational awareness products, to the maximum extent practicable; and\n**(3)**\nnot less frequently than every 3 years, shall review the basic space situational awareness services described in paragraph (1) to ensure that such services provided by the Federal Government do not compete with space situational awareness services offered by the private sector.\n##### (f) Requirements for data acquisition and dissemination\nIn acquiring data, analytics, information, and services under subsection (c) and disseminating data, analytics, information, and services under subsections (d) and (e), the Assistant Secretary of Commerce for Space Commerce shall\u2014\n**(1)**\nleverage commercial capabilities to the maximum extent practicable;\n**(2)**\nprioritize the acquisition of data, analytics, information, and services from commercial industry located in or licensed in the United States to supplement data collected by United States Government agencies, including the Department of Defense and the National Aeronautics and Space Administration;\n**(3)**\nappropriately protect proprietary data, information, and systems of firms located in the United States, including by using appropriate infrastructure and cybersecurity measures, including measures set forth in the most recent version of the Cybersecurity Framework, or successor document, maintained by the National Institute of Standards and Technology;\n**(4)**\nfacilitate the development of standardization and consistency in data reporting, in collaboration with satellite owners and operators, commercial space situational awareness data and service providers, the academic community, nonprofit organizations, and the Director of the National Institute of Standards and Technology; and\n**(5)**\nencourage foreign governments to participate in unclassified data sharing arrangements for space situational awareness and space traffic coordination.\n##### (g) Other transaction authority\nIn carrying out the activities required by this section, the Secretary of Commerce shall enter into such contracts, leases, cooperative agreements, or other transactions as may be necessary.\n##### (h) Space object defined\nIn this section, the term space object means any object launched into space, or created in space, robotically or by humans, including an object\u2019s component parts.\n#### 3. Office of Space Commerce\n##### (a) Definitions\n**(1) In general**\nSection 50701 of title 51, United States Code, is amended to read as follows:\n50701. Definitions In this chapter: (1) Assistant Secretary The term Assistant Secretary means the Assistant Secretary of Commerce for Space Commerce. (2) Bureau The term Bureau means the Bureau of Space Commerce established under section 50702. (3) Orbital debris The term orbital debris \u2014 (A) means\u2014 (i) any human-made space object orbiting Earth that\u2014 (I) no longer serves an intended purpose; (II) has reached the end of its mission; or (III) is incapable of safe maneuver or operation; and (ii) a rocket body and other hardware left in orbit as a result of normal launch and operational activities; and (B) includes fragmentation debris produced by failure or collision of human-made space objects. (4) Secretary The term Secretary means the Secretary of Commerce. (5) Space object The term space object means any object launched into space or created in space robotically or by humans, including the component parts of such an object. (6) Space situational awareness The term space situational awareness means\u2014 (A) the identification, characterization, tracking, and the predicted movement and behavior of space objects and orbital debris; and (B) the understanding of the space operational environment. (7) Space traffic coordination The term space traffic coordination means the planning, assessment, and coordination of activities to enhance the safety, stability, and sustainability of operations in the space environment. .\n**(2) Clerical amendment**\nThe table of sections for chapter 507 of title 51, United States Code, is amended by striking the item relating to section 50701 and inserting the following:\n50701. Definitions. .\n##### (b) Transition of Office to Bureau\nSubsection (a) of section 50702 of title 51, United States Code, is amended by inserting before the period at the end the following: , which, not later than 5 years after the date of the enactment of this Act, shall be elevated by the Secretary of Commerce from an office within the National Oceanic and Atmospheric Administration to a bureau reporting directly to the Office of the Secretary of Commerce .\n##### (c) Additional functions of Bureau\nSubsection (c) of such section is amended\u2014\n**(1)**\nin paragraph (4), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(6) to perform space situational awareness and space traffic management duties pursuant to the SAFE Orbit Act . .\n##### (d) Assistant Secretary of Commerce for Space Commerce\n**(1) In general**\nSubsection (b) of such section is amended to read as follows:\n(b) Assistant Secretary The Bureau shall be headed by the Assistant Secretary of Commerce for Space Commerce, who shall\u2014 (1) be appointed by the President, by and with the advice and consent of the Senate; (2) report directly to the Secretary of Commerce; and (3) have a rate of pay that is equal to the rate payable for level IV of the Executive Schedule under section 5315 of title 5. .\n**(2) Conforming amendments**\n**(A)**\nSection 50702(d) of title 51, United States Code, is amended\u2014\n**(i)**\nin the subsection heading, by striking Director and inserting Assistant Secretary ; and\n**(ii)**\nin the matter preceding paragraph (1), by striking Director and inserting Assistant Secretary .\n**(B)**\nSection 5315 of title 5, United States Code, is amended by striking Assistant Secretaries of Commerce (11) and inserting Assistant Secretaries of Commerce (12) .\n**(3) References**\nOn and after the date of the enactment of this Act, any reference in any law or regulation to the Director of the Office of Space Commerce shall be deemed to be a reference to the Assistant Secretary of Commerce for Space Commerce.\n##### (e) Transition report\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Commerce shall submit to the appropriate committees of Congress a report that sets forth transition and continuity of operations plans for the functional and administrative transfer of the Office of Space Commerce from the National Oceanic and Atmospheric Administration to a bureau reporting to the Office of the Secretary of Commerce.\n**(2) Goal**\nThe goal of transition and continuity of operations planning shall be to minimize the cost and administrative burden of establishing the Bureau of Space Commerce while maximizing the efficiency and effectiveness of the functions and responsibilities of the Bureau of Space Commerce, in accordance with this section and the amendments made by this section.\n**(3) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Science, Space, and Technology and the Committee on Appropriations of the House of Representatives.",
      "versionDate": "2025-02-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s428rs.xml",
      "text": "II\nCalendar No. 170\n119th CONGRESS\n1st Session\nS. 428\n[Report No. 119\u201365]\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Cornyn (for himself, Mr. Peters , Mr. Wicker , Mrs. Blackburn , Mr. Hickenlooper , Mr. Kelly , Mr. Schmitt , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 29, 2025 Reported by Mr. Cruz , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo promote space situational awareness and space traffic coordination and to modify the functions and leadership of the Office of Space Commerce, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Situational Awareness of Flying Elements in Orbit Act or the SAFE Orbit Act .\n#### 2. Space situational awareness and space traffic coordination\n##### (a) In general\nThe Secretary of Commerce shall facilitate safe operations in space and encourage the development of commercial space capabilities by acquiring and disseminating unclassified data, analytics, information, and services on space activities.\n##### (b) Immunity\nThe United States, any agencies and instrumentalities thereof, and any individuals, firms, corporations, and other persons acting for the United States Government, including nongovernmental entities, shall be immune from any suit in any court for any cause of action arising from the provision or receipt of space situational awareness services or information, whether or not provided in accordance with this section, or any related action or omission.\n##### (c) Acquisition of data\nThe Assistant Secretary of Commerce for Space Commerce (established under section 50702(b) of title 51, United States Code, as amended by section 3) is authorized to acquire\u2014\n**(1)**\ndata, analytics, information, and services, including with respect to\u2014\n**(A)**\nlocation tracking data;\n**(B)**\npositional and orbit determination information; and\n**(C)**\nconjunction data messages; and\n**(2)**\nsuch other data, analytics, information, and services as the Secretary of Commerce determines necessary to avoid collisions of space objects.\n##### (d) Database on satellite location and behavior\nThe Assistant Secretary of Commerce for Space Commerce shall provide access for the public, at no charge, to a fully updated, unclassified database of information concerning space objects and behavior that includes\u2014\n**(1)**\nthe data and information acquired under subsection (c), except to the extent that such data or information is classified or a trade secret (as defined in section 1839 of title 18, United States Code); and\n**(2)**\nthe provision of basic space situational awareness services and space traffic coordination based on the data referred to in paragraph (1), including basic analytics, tracking calculations, and conjunction data messages.\n##### (e) Basic space situational awareness services\nThe Assistant Secretary of Commerce for Space Commerce\u2014\n**(1)**\nshall provide to satellite operators, at no charge, basic space situational awareness services, including the data, analytics, information, and services described in subsection (c);\n**(2)**\nin carrying out paragraph (1), may not compete with private sector space situational awareness products, to the maximum extent practicable; and\n**(3)**\nnot less frequently than every 3 years, shall review the basic space situational awareness services described in paragraph (1) to ensure that such services provided by the Federal Government do not compete with space situational awareness services offered by the private sector.\n##### (f) Requirements for data acquisition and dissemination\nIn acquiring data, analytics, information, and services under subsection (c) and disseminating data, analytics, information, and services under subsections (d) and (e), the Assistant Secretary of Commerce for Space Commerce shall\u2014\n**(1)**\nleverage commercial capabilities to the maximum extent practicable;\n**(2)**\nprioritize the acquisition of data, analytics, information, and services from commercial industry located in or licensed in the United States to supplement data collected by United States Government agencies, including the Department of Defense and the National Aeronautics and Space Administration;\n**(3)**\nappropriately protect proprietary data, information, and systems of firms located in the United States, including by using appropriate infrastructure and cybersecurity measures, including measures set forth in the most recent version of the Cybersecurity Framework, or successor document, maintained by the National Institute of Standards and Technology;\n**(4)**\nfacilitate the development of standardization and consistency in data reporting, in collaboration with satellite owners and operators, commercial space situational awareness data and service providers, the academic community, nonprofit organizations, and the Director of the National Institute of Standards and Technology; and\n**(5)**\nencourage foreign governments to participate in unclassified data sharing arrangements for space situational awareness and space traffic coordination.\n##### (g) Other transaction authority\nIn carrying out the activities required by this section, the Secretary of Commerce shall enter into such contracts, leases, cooperative agreements, or other transactions as may be necessary.\n##### (h) Space object defined\nIn this section, the term space object means any object launched into space, or created in space, robotically or by humans, including an object\u2019s component parts.\n#### 3. Office of Space Commerce\n##### (a) Definitions\n**(1) In general**\nSection 50701 of title 51, United States Code, is amended to read as follows:\n50701. Definitions In this chapter: (1) Assistant Secretary The term Assistant Secretary means the Assistant Secretary of Commerce for Space Commerce. (2) Bureau The term Bureau means the Bureau of Space Commerce established under section 50702. (3) Orbital debris The term orbital debris \u2014 (A) means\u2014 (i) any human-made space object orbiting Earth that\u2014 (I) no longer serves an intended purpose; (II) has reached the end of its mission; or (III) is incapable of safe maneuver or operation; and (ii) a rocket body and other hardware left in orbit as a result of normal launch and operational activities; and (B) includes fragmentation debris produced by failure or collision of human-made space objects. (4) Secretary The term Secretary means the Secretary of Commerce. (5) Space object The term space object means any object launched into space or created in space , robotically or by humans, including the component parts of such an object. (6) Space situational awareness The term space situational awareness means\u2014 (A) the identification, characterization, tracking, and the predicted movement and behavior of space objects and orbital debris; and (B) the understanding of the space operational environment. (7) Space traffic coordination The term space traffic coordination means the planning, assessment, and coordination of activities to enhance the safety, stability, and sustainability of operations in the space environment. .\n**(2) Clerical amendment**\nThe table of sections for chapter 507 of title 51, United States Code, is amended by striking the item relating to section 50701 and inserting the following:\n50701. Definitions. .\n##### (b) Transition of Office to Bureau\nSubsection (a) of section 50702 of title 51, United States Code, is amended by inserting before the period at the end the following: , which, not later than 5 years after the date of the enactment of the SAFE Orbit Act this Act , shall be elevated by the Secretary of Commerce from an office within the National Oceanic and Atmospheric Administration to a bureau reporting directly to the Office of the Secretary of Commerce .\n##### (c) Additional functions of Bureau\nSubsection (c) of such section is amended\u2014\n**(1)**\nin paragraph (4), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(6) to perform space situational awareness and space traffic management duties pursuant to the SAFE Orbit Act . .\n##### (d) Assistant Secretary of Commerce for Space Commerce\n**(1) In general**\nSubsection (b) of such section is amended to read as follows:\n(b) Assistant Secretary The Bureau shall be headed by the Assistant Secretary of Commerce for Space Commerce, who shall\u2014 (1) be appointed by the President, by and with the advice and consent of the Senate; (2) report directly to the Secretary of Commerce; and (3) have a rate of pay that is equal to the rate payable for level IV of the Executive Schedule under section 5315 of title 5. .\n**(2) Conforming amendments**\n**(A)**\nSection 50702(d) of title 51, United States Code, is amended\u2014\n**(i)**\nin the subsection heading, by striking Director and inserting Assistant Secretary ; and\n**(ii)**\nin the matter preceding paragraph (1), by striking Director and inserting Assistant Secretary .\n**(B)**\nSection 5315 of title 5, United States Code, is amended by striking Assistant Secretaries of Commerce (11) and inserting Assistant Secretaries of Commerce (12) .\n**(3) References**\nOn and after the date of the enactment of this Act, any reference in any law or regulation to the Director of the Office of Space Commerce shall be deemed to be a reference to the Assistant Secretary of Commerce for Space Commerce.\n##### (e) Transition report\n##### (e) Office of Space Commerce staffing\n**(1) Required staff levels during Office to Bureau transition**\nNot later than 30 days after the date of the enactment of this Act, and annually thereafter until the date that is 1 year after the date on which the transition from office to bureau is complete, the Secretary of Commerce (referred to in this subsection as the Secretary ) and the Assistant Secretary of Commerce for Space Commerce (referred to in this subsection as the Assistant Secretary ) shall\u2014\n**(A)**\ncomplete a staffing plan for the Office of Space Commerce, consistent with the functions described in section 50702 of title 51, United States Code, as amended by this Act, and the transition from an office to a bureau; and\n**(B)**\nsubmit such plan to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives.\n**(2) Notification of terminations not based on performance**\nSubject to the availability of appropriations, the Secretary or the Assistant Secretary shall not reduce the number of full-time equivalent positions in the Office of Space Commerce or the Bureau of Space Commerce for any reason other than performance without prior notification to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives.\n##### (f) Transition report\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Commerce shall submit to the appropriate committees of Congress a report that sets forth transition and continuity of operations plans for the functional and administrative transfer of the Office of Space Commerce from the National Oceanic and Atmospheric Administration to a bureau reporting to the Office of the Secretary of Commerce.\n**(2) Goal**\nThe goal of transition and continuity of operations planning shall be to minimize the cost and administrative burden of establishing the Bureau of Space Commerce while maximizing the efficiency and effectiveness of the functions and responsibilities of the Bureau of Space Commerce, in accordance with this section and the amendments made by this section.\n**(3) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Science, Space, and Technology and the Committee on Appropriations of the House of Representatives.",
      "versionDate": "2025-09-29",
      "versionType": "Reported in Senate"
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-03-20T14:25:04Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-20T14:25:04Z"
          },
          {
            "name": "Department of Commerce",
            "updateDate": "2025-03-20T14:25:04Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-03-20T14:25:04Z"
          },
          {
            "name": "International scientific cooperation",
            "updateDate": "2025-03-20T14:25:04Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-03-20T14:25:04Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2025-03-20T14:25:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-10T18:12:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
    "originChamber": "Senate",
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
          "measure-id": "id119s428",
          "measure-number": "428",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s428v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Situational Awareness of Flying Elements in Orbit Act or the SAFE Orbit Act</strong></p><p>This bill provides statutory authority for the Traffic Coordination System for Space, which is being developed by the Office of Space Commerce to provide space situational awareness data and services to space operators. (<em>Space situational awareness</em> means an understanding of the space operational environment and the identification, tracking, and prediction of the behavior of space objects and debris.)</p><p>As an initial matter, the bill provides for the elevation of the Office of Space Commerce to a standalone bureau within the Department of Commerce. (The office currently sits within the National Oceanic and Atmospheric Administration.)</p><p>The bill authorizes the bureau to acquire location tracking data, positional and orbit determination information, conjunction data messages, and other data, analytics, information, and services deemed necessary to avoid collisions in space. The bureau must disseminate this information at no charge (1) through a public database of space situational awareness information and services, including space traffic coordination; and (2) through the provision of basic situational awareness services to satellite operators. The bill also sets forth certain requirements for the collection and dissemination of such information, including that, to the extent practicable, the provision of service to satellite operators may not compete with private situational awareness products.</p><p>Finally, the bill provides immunity for the United States government from any suit for a cause of action arising from the provision or receipt of space situational awareness services or information.</p>"
        },
        "title": "SAFE Orbit Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s428.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Situational Awareness of Flying Elements in Orbit Act or the SAFE Orbit Act</strong></p><p>This bill provides statutory authority for the Traffic Coordination System for Space, which is being developed by the Office of Space Commerce to provide space situational awareness data and services to space operators. (<em>Space situational awareness</em> means an understanding of the space operational environment and the identification, tracking, and prediction of the behavior of space objects and debris.)</p><p>As an initial matter, the bill provides for the elevation of the Office of Space Commerce to a standalone bureau within the Department of Commerce. (The office currently sits within the National Oceanic and Atmospheric Administration.)</p><p>The bill authorizes the bureau to acquire location tracking data, positional and orbit determination information, conjunction data messages, and other data, analytics, information, and services deemed necessary to avoid collisions in space. The bureau must disseminate this information at no charge (1) through a public database of space situational awareness information and services, including space traffic coordination; and (2) through the provision of basic situational awareness services to satellite operators. The bill also sets forth certain requirements for the collection and dissemination of such information, including that, to the extent practicable, the provision of service to satellite operators may not compete with private situational awareness products.</p><p>Finally, the bill provides immunity for the United States government from any suit for a cause of action arising from the provision or receipt of space situational awareness services or information.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s428"
    },
    "title": "SAFE Orbit Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Situational Awareness of Flying Elements in Orbit Act or the SAFE Orbit Act</strong></p><p>This bill provides statutory authority for the Traffic Coordination System for Space, which is being developed by the Office of Space Commerce to provide space situational awareness data and services to space operators. (<em>Space situational awareness</em> means an understanding of the space operational environment and the identification, tracking, and prediction of the behavior of space objects and debris.)</p><p>As an initial matter, the bill provides for the elevation of the Office of Space Commerce to a standalone bureau within the Department of Commerce. (The office currently sits within the National Oceanic and Atmospheric Administration.)</p><p>The bill authorizes the bureau to acquire location tracking data, positional and orbit determination information, conjunction data messages, and other data, analytics, information, and services deemed necessary to avoid collisions in space. The bureau must disseminate this information at no charge (1) through a public database of space situational awareness information and services, including space traffic coordination; and (2) through the provision of basic situational awareness services to satellite operators. The bill also sets forth certain requirements for the collection and dissemination of such information, including that, to the extent practicable, the provision of service to satellite operators may not compete with private situational awareness products.</p><p>Finally, the bill provides immunity for the United States government from any suit for a cause of action arising from the provision or receipt of space situational awareness services or information.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119s428"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s428is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s428rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "SAFE Orbit Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Situational Awareness of Flying Elements in Orbit Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:13Z"
    },
    {
      "title": "SAFE Orbit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Orbit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Situational Awareness of Flying Elements in Orbit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote space situational awareness and space traffic coordination and to modify the functions and leadership of the Office of Space Commerce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:18:23Z"
    }
  ]
}
```
